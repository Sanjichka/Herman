"""
Ask one question and see which chunks come back, with their scores.

Usage:
    uv run python src/search.py "How do I add a VAT percentage?"
    uv run python src/search.py "reset a password" --k 8 --source manual
"""

import argparse

from common import embed, get_conn, to_pgvector


def search(question: str, k: int = 5, source: str | None = None):
    vec = to_pgvector(embed([question])[0])
    # <=> is cosine distance, the same operator Spring AI uses; score = 1 - distance
    sql = """
        SELECT id, content, metadata, 1 - (embedding <=> %s::vector) AS score
        FROM vector_store
        {where}
        ORDER BY embedding <=> %s::vector
        LIMIT %s
    """
    where, params = "", [vec]
    if source:
        where = "WHERE metadata->>'source' = %s"
        params.append(source)
    params += [vec, k]
    with get_conn() as conn:
        return conn.execute(sql.format(where=where), params).fetchall()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--source", choices=["manual", "support_history"])
    args = ap.parse_args()

    for rank, (_id, content, meta, score) in enumerate(search(args.question, args.k, args.source), 1):
        path = " > ".join(meta["section_path"])
        first_line = content.split("\n\n", 1)[-1].replace("\n", " ")[:110]
        print(f"{rank}. {score:.3f}  {path}")
        print(f"          {first_line}...")


if __name__ == "__main__":
    main()
