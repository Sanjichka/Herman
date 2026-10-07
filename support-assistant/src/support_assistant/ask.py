"""
RAG answer: retrieve relevant chunks, then generate a grounded answer.

The flow is a LangGraph graph with three nodes:
  retrieve → filter_chunks → generate
filter_chunks short-circuits to a refusal if no chunks pass the threshold.

Usage (CLI):
    uv run python src/support_assistant/ask.py "How do I add a VAT percentage?"
    uv run python src/support_assistant/ask.py "reset a password" --k 8 --threshold 0.40
"""

import argparse
import os
import re
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from openai import OpenAI

from common import get_conn
from search import search

SIMILARITY_THRESHOLD = 0.35
GENERATION_MODEL = "gpt-4o-mini"
REFUSAL = "I don't have enough information to answer that. Please contact your support team."

SYSTEM_PROMPT = """\
You are Herman, a support assistant for a medical software product.
You answer questions using ONLY the manual excerpts provided below.
Rules:
- Cite the manual section (e.g. "According to Finance > VAT > Add VAT percentage, ...") in every factual sentence.
- Users describe things in everyday language; the software uses domain-specific terms. \
Treat concepts as equivalent when they refer to the same real-world thing. \
Use the excerpts to answer, and when you bridge terminology, name the software's term \
so the user learns it (e.g. "What you call a 'product' is referred to as a 'declaration code' in this software.").
- Never use general knowledge to add facts, steps or instructions not present in the excerpts.
- Before refusing, ask yourself: does any excerpt address what the user is trying to accomplish, \
even if the software uses different terminology? Only refuse if no excerpt is even loosely relevant \
to the underlying goal. If so, respond with exactly:
  "I don't have enough information to answer that. Please contact your support team."
- Be concise and direct.
"""


class RAGState(TypedDict):
    question: str
    k: int
    threshold: float
    raw_chunks: list
    passing_chunks: list
    answer: str
    refused: bool


def retrieve(state: RAGState) -> dict:
    results = search(state["question"], k=state["k"])
    return {"raw_chunks": results}


def filter_chunks(state: RAGState) -> dict:
    passing = [
        (id_, content, meta, score)
        for id_, content, meta, score in state["raw_chunks"]
        if score >= state["threshold"]
    ]
    if not passing:
        return {
            "passing_chunks": [],
            "answer": REFUSAL,
            "refused": True,
        }
    return {"passing_chunks": passing}


def expand_references(state: RAGState) -> dict:
    """
    Scan retrieved chunks for (see: Section Name) cross-references and
    fetch those sections from the DB, so the LLM sees the full picture
    when an answer spans multiple manual sections.
    """
    existing_ids = {row[0] for row in state["passing_chunks"]}
    refs = set()
    for _, content, _, _ in state["passing_chunks"]:
        for match in re.finditer(r"\(see:\s*([^)]+)\)", content, re.IGNORECASE):
            refs.add(match.group(1).strip())

    if not refs:
        return {}

    from common import embed, to_pgvector
    question_vec = to_pgvector(embed([state["question"]])[0])

    extra = []
    with get_conn() as conn:
        for ref in refs:
            rows = conn.execute(
                """
                SELECT id, content, metadata,
                       1 - (embedding <=> %s::vector) AS score
                FROM vector_store
                WHERE (metadata->'section_path') @> to_jsonb(%s::text)
                   OR metadata->>'section_title' ILIKE %s
                ORDER BY score DESC
                LIMIT 4
                """,
                [question_vec, ref, ref],
            ).fetchall()
            for row in rows:
                if row[0] not in existing_ids:
                    extra.append(row)
                    existing_ids.add(row[0])

    if not extra:
        return {}
    return {"passing_chunks": state["passing_chunks"] + extra}


def generate(state: RAGState) -> dict:
    context_blocks = []
    chunk_metas = []
    for _, content, meta, score in state["passing_chunks"]:
        section = " > ".join(meta.get("section_path", [meta.get("section_title", "Unknown")]))
        context_blocks.append(f"[{section}]\n{content}")
        chunk_metas.append({**meta, "score": score})

    context = "\n\n---\n\n".join(context_blocks)
    user_message = f"Manual excerpts:\n\n{context}\n\n---\n\nQuestion: {state['question']}"

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0,
    )

    answer = response.choices[0].message.content.strip()
    refused = answer.startswith("I don't have enough information")
    return {"answer": answer, "refused": refused, "passing_chunks": chunk_metas}


def _route_after_filter(state: RAGState) -> str:
    return "expand_references" if state["passing_chunks"] else END


def _build_graph():
    g = StateGraph(RAGState)
    g.add_node("retrieve", retrieve)
    g.add_node("filter_chunks", filter_chunks)
    g.add_node("expand_references", expand_references)
    g.add_node("generate", generate)
    g.add_edge(START, "retrieve")
    g.add_edge("retrieve", "filter_chunks")
    g.add_conditional_edges("filter_chunks", _route_after_filter)
    g.add_edge("expand_references", "generate")
    g.add_edge("generate", END)
    return g.compile()


_graph = _build_graph()


def ask(question: str, k: int = 5, threshold: float = SIMILARITY_THRESHOLD) -> dict:
    """
    Returns {"answer": str, "chunks": list[dict], "refused": bool}
    """
    result = _graph.invoke({
        "question": question,
        "k": k,
        "threshold": threshold,
        "raw_chunks": [],
        "passing_chunks": [],
        "answer": "",
        "refused": False,
    })
    return {
        "answer": result["answer"],
        "chunks": result["passing_chunks"],
        "refused": result["refused"],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("question")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--threshold", type=float, default=SIMILARITY_THRESHOLD)
    ap.add_argument("--raw", action="store_true", help="print retrieved chunks without LLM generation")
    args = ap.parse_args()

    if args.raw:
        chunks = search(args.question, k=args.k)
        passing = [(id_, content, meta, score) for id_, content, meta, score in chunks if score >= args.threshold]
        if not passing:
            print("No chunks above threshold.")
            return
        for i, (_, content, meta, score) in enumerate(passing, 1):
            path = " > ".join(meta.get("section_path", [meta.get("section_title", "Unknown")]))
            print(f"[{i}] {score:.3f}  {path}\n{content}\n")
        return

    result = ask(args.question, k=args.k, threshold=args.threshold)
    print(result["answer"])
    if not result["refused"]:
        print(f"\n--- Sources ({len(result['chunks'])}) ---")
        for c in result["chunks"]:
            path = " > ".join(c.get("section_path", []))
            print(f"  {c['score']:.3f}  {path}")


if __name__ == "__main__":
    main()
