"""
Embed support ticket history and load it into vector_store.

Usage:
    uv run python src/ingest_tickets.py knowledge/tickets/support_history.csv --dry-run
    uv run python src/ingest_tickets.py knowledge/tickets/support_history.csv

--dry-run   builds chunks and writes a preview, without calling the API or the database.

Input CSV columns: ticket_id, date, category, question, answer
One row = one resolved support ticket = one chunk.

Re-running is safe: all support_history chunks are replaced, not duplicated.
A readable preview of every chunk is always written to knowledge/chunks/.
"""

import argparse
import csv
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from common import CHUNKING_VERSION, EMBED_MODEL, embed, get_conn, n_tokens, to_pgvector

DOC_ID = "support_tickets"
ID_NAMESPACE = uuid.UUID("3a7f1c2e-8b4d-4f9a-9e6c-1d5b2a3c7f08")


def build_chunks(path: Path) -> list[dict]:
    chunks = []
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            content = (
                f"Support ticket: {row['category']}\n\n"
                f"Q: {row['question']}\n\n"
                f"A: {row['answer']}"
            )
            chunk_id = uuid.uuid5(ID_NAMESPACE, f"{DOC_ID}|{row['ticket_id']}|{CHUNKING_VERSION}")
            chunks.append(
                {
                    "id": str(chunk_id),
                    "content": content,
                    "metadata": {
                        "source": "support_history",
                        "doc_id": DOC_ID,
                        "ticket_id": row["ticket_id"],
                        "date": row["date"],
                        "category": row["category"],
                        "tokens": n_tokens(content),
                        "content_hash": hashlib.sha256(content.encode()).hexdigest()[:16],
                        "chunking_version": CHUNKING_VERSION,
                        "embedding_model": EMBED_MODEL,
                        "ingested_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    },
                }
            )
    return chunks


def write_preview(chunks: list[dict]) -> Path:
    out_dir = Path("knowledge/chunks")
    out_dir.mkdir(parents=True, exist_ok=True)
    md = out_dir / f"{DOC_ID}.chunks.md"
    jl = out_dir / f"{DOC_ID}.chunks.jsonl"
    with md.open("w", encoding="utf-8") as f:
        for n, c in enumerate(chunks, 1):
            m = c["metadata"]
            f.write(f"<!-- chunk {n} | {m['tokens']} tokens | ticket {m['ticket_id']} -->\n")
            f.write(c["content"] + "\n\n---\n\n")
    with jl.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    return md


def load(chunks: list[dict]) -> None:
    print(f"Embedding {len(chunks)} chunks with {EMBED_MODEL}...")
    vectors = embed([c["content"] for c in chunks])

    from psycopg.types.json import Json

    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM vector_store WHERE metadata->>'source' = 'support_history'")
        print(f"Removed {cur.rowcount} old chunks.")
        cur.executemany(
            "INSERT INTO vector_store (id, content, metadata, embedding) VALUES (%s, %s, %s, %s::vector)",
            [(c["id"], c["content"], Json(c["metadata"]), to_pgvector(v)) for c, v in zip(chunks, vectors)],
        )
    print(f"Inserted {len(chunks)} chunks.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tickets", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    chunks = build_chunks(args.tickets)
    if not chunks:
        raise SystemExit("No chunks built — is the CSV empty or missing required columns?")

    preview = write_preview(chunks)
    sizes = [c["metadata"]["tokens"] for c in chunks]
    print(f"{len(chunks)} chunks | tokens min {min(sizes)}, median {sorted(sizes)[len(sizes)//2]}, max {max(sizes)}")
    print(f"Preview: {preview}")

    if not args.dry_run:
        load(chunks)


if __name__ == "__main__":
    main()
