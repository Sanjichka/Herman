"""
RAG answer: retrieve relevant chunks, then generate a grounded answer.

Usage (CLI):
    uv run python src/support_assistant/ask.py "How do I add a VAT percentage?"
    uv run python src/support_assistant/ask.py "reset a password" --k 8 --threshold 0.40
"""

import argparse
import os

from openai import OpenAI

from search import search

SIMILARITY_THRESHOLD = 0.35
GENERATION_MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = """\
You are Herman, a support assistant for a medical software product.
You answer questions using ONLY the manual excerpts provided below.
Rules:
- Cite the manual section (e.g. "According to Finance > VAT > Add VAT percentage, ...") in every factual sentence.
- If the provided excerpts do not contain enough information to answer, respond with exactly:
  "I don't have enough information to answer that. Please contact your support team."
- Never guess or infer beyond what the excerpts say.
- Be concise and direct.
"""


def ask(question: str, k: int = 5, threshold: float = SIMILARITY_THRESHOLD) -> dict:
    """
    Returns {"answer": str, "chunks": list[dict], "refused": bool}
    """
    results = search(question, k=k)

    # Filter by similarity threshold
    passing = [(id_, content, meta, score) for id_, content, meta, score in results if score >= threshold]

    if not passing:
        return {
            "answer": "I don't have enough information to answer that. Please contact your support team.",
            "chunks": [],
            "refused": True,
        }

    context_blocks = []
    chunk_metas = []
    for _, content, meta, score in passing:
        section = " > ".join(meta.get("section_path", [meta.get("section_title", "Unknown")]))
        context_blocks.append(f"[{section}]\n{content}")
        chunk_metas.append({**meta, "score": score})

    context = "\n\n---\n\n".join(context_blocks)
    user_message = f"Manual excerpts:\n\n{context}\n\n---\n\nQuestion: {question}"

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
    return {"answer": answer, "chunks": chunk_metas, "refused": refused}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("question")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--threshold", type=float, default=SIMILARITY_THRESHOLD)
    args = ap.parse_args()

    result = ask(args.question, k=args.k, threshold=args.threshold)
    print(result["answer"])
    if not result["refused"]:
        print(f"\n--- Sources ({len(result['chunks'])}) ---")
        for c in result["chunks"]:
            path = " > ".join(c.get("section_path", []))
            print(f"  {c['score']:.3f}  {path}")


if __name__ == "__main__":
    main()
