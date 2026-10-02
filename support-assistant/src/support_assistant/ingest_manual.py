"""
Chunk a cleaned manual, embed the chunks and load them into vector_store.

Usage:
    uv run python src/ingest_manual.py knowledge/manual/Manual_Configuration_INT.md --dry-run
    uv run python src/ingest_manual.py knowledge/manual/Manual_Configuration_INT.md --chapter Finance
    uv run python src/ingest_manual.py knowledge/manual/Manual_Configuration_INT.md

--dry-run   makes the chunks and writes a preview, without calling the API or the database.
--chapter   ingests one top-level chapter only (case-insensitive).

Re-running is safe: the chunks of this manual (or chapter) are replaced, not duplicated.
A readable preview of every chunk is always written to knowledge/chunks/.

How chunking works (chunking_version in common.py):
  1. Every heading starts a new section. A section's text is what sits between
     its heading and the next heading, of any level.
  2. Each chunk starts with its breadcrumb, e.g.
     "Manual section: Finance > VAT > Add VAT percentage", so that a chunk
     like "Single item" still knows it is about the price matrix.
  3. Sections longer than --max-tokens are split at paragraph boundaries.
     Tables are kept whole; a table that is too long is split by rows,
     repeating its header row in every part. A long list is split between items.
  4. A very short intro above subsections is merged into the first subsection.
"""

import argparse
import hashlib
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from common import CHUNKING_VERSION, EMBED_MODEL, embed, get_conn, n_tokens, to_pgvector

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)
EXCLUDED_CHAPTERS = {"disclaimer"}
MIN_WORDS = 5
SHORT_INTRO_TOKENS = 40
ID_NAMESPACE = uuid.UUID("6f1c2b1e-9a57-4c4e-8f1e-3d2a8b7c9e01")

def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# ---------- Parsing ----------

def read_manual(path: Path):
    raw = path.read_text(encoding="utf-8")
    meta = {}
    m = FRONT_MATTER.match(raw)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        raw = raw[m.end():]
    return meta, raw


def split_sections(text: str):
    """Yield (path, level, body) for every heading. Text before the first heading is skipped."""
    stack, body, current = [], [], None
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            if current:
                yield current[0], current[1], "\n".join(body).strip()
            level, title = len(m.group(1)), m.group(2)
            stack = [s for s in stack if s[0] < level] + [(level, title)]
            current = ([t for _, t in stack], level)
            body = []
        elif current:
            body.append(line)
    if current:
        yield current[0], current[1], "\n".join(body).strip()


# ---------- Splitting long sections ----------

def blocks(body: str):
    """Paragraphs, but a table or a numbered/bulleted list stays one block."""
    out, cur, kind = [], [], None
    for line in body.splitlines():
        if not line.strip():
            if kind == "table" or not cur:
                if cur:
                    out.append((kind, cur))
                cur, kind = [], None
            else:
                cur.append(line)  # blank lines inside a list/paragraph run
            continue
        k = "table" if line.lstrip().startswith("|") else "text"
        if cur and k != kind:
            out.append((kind, cur))
            cur = []
        cur.append(line)
        kind = k
    if cur:
        out.append((kind, cur))
    return [(k, "\n".join(ls).strip()) for k, ls in out]


def split_table(table: str, max_tokens: int):
    rows = table.splitlines()
    header, data = rows[:2], rows[2:]
    parts, cur = [], []
    for row in data:
        if cur and n_tokens("\n".join(header + cur + [row])) > max_tokens:
            parts.append("\n".join(header + cur))
            cur = []
        cur.append(row)
    if cur:
        parts.append("\n".join(header + cur))
    return parts


def list_items(text: str):
    """Split at lines that start at column 0; indented sub-lines stay with their item."""
    items, cur = [], []
    for line in text.splitlines():
        if cur and line and not line[0].isspace():
            items.append("\n".join(cur))
            cur = []
        cur.append(line)
    if cur:
        items.append("\n".join(cur))
    return items


def split_body(body: str, max_tokens: int):
    if n_tokens(body) <= max_tokens:
        return [body]
    pieces = []
    for kind, block in blocks(body):
        if kind == "table" and n_tokens(block) > max_tokens:
            pieces.extend(split_table(block, max_tokens))
        elif kind == "text" and n_tokens(block) > max_tokens:
            for para in (p for p in re.split(r"\n\s*\n", block) if p.strip()):
                if n_tokens(para) > max_tokens:
                    pieces.extend(list_items(para))  # a long list: split between items
                else:
                    pieces.append(para)
        else:
            pieces.append(block)
    parts, cur = [], ""
    for p in pieces:
        candidate = f"{cur}\n\n{p}" if cur else p
        if cur and n_tokens(candidate) > max_tokens:
            parts.append(cur)
            cur = p
        else:
            cur = candidate
    if cur:
        parts.append(cur)
    return parts


# ---------- Building chunks ----------

def build_chunks(path: Path, max_tokens: int, chapter: str | None):
    meta, text = read_manual(path)
    doc_id = path.stem
    manual_version = meta.get("manual_version", "unknown")
    chunks, seen_keys = [], {}

    # A short intro like "To change prices, do the following." is useless on its own:
    # it is carried into the first subsection below it instead.
    sections = list(split_sections(text))
    merged, carry = [], None
    for idx, (heading_path, level, body) in enumerate(sections):
        if carry and heading_path[: len(carry[0])] == carry[0]:
            body = f"{carry[1]}\n\n{body}".strip()
        carry = None
        nxt = sections[idx + 1] if idx + 1 < len(sections) else None
        is_parent = nxt is not None and len(nxt[0]) > len(heading_path) and nxt[0][: len(heading_path)] == heading_path
        if is_parent and body and n_tokens(body) < SHORT_INTRO_TOKENS:
            carry = (heading_path, body)
            continue
        merged.append((heading_path, level, body))

    for heading_path, level, body in merged:
        top = heading_path[0]
        if top.lower() in EXCLUDED_CHAPTERS:
            continue
        if chapter and top.lower() != chapter.lower():
            continue
        if len(body.split()) < MIN_WORDS:
            continue  # heading with no real content of its own

        breadcrumb = " > ".join(heading_path)
        key = slug(breadcrumb)
        seen_keys[key] = seen_keys.get(key, 0) + 1
        if seen_keys[key] > 1:  # same heading path twice: keep keys unique
            key = f"{key}-{seen_keys[key]}"

        parts = split_body(body, max_tokens)
        for i, part in enumerate(parts):
            content = f"Manual section: {breadcrumb}\n\n{part}"
            chunk_id = uuid.uuid5(ID_NAMESPACE, f"{doc_id}|{key}|{i}|{CHUNKING_VERSION}")
            chunks.append(
                {
                    "id": str(chunk_id),
                    "content": content,
                    "metadata": {
                        "source": "manual",
                        "doc_id": doc_id,
                        "source_file": meta.get("source_file", path.name),
                        "manual_version": manual_version,
                        "chapter": top,
                        "section_path": heading_path,
                        "section_title": heading_path[-1],
                        "section_key": key,
                        "heading_level": level,
                        "part": i + 1,
                        "parts": len(parts),
                        "has_table": "|" in part and "---" in part,
                        "has_steps": bool(re.search(r"^\d+\.\s", part, re.M)),
                        "tokens": n_tokens(content),
                        "content_hash": hashlib.sha256(content.encode()).hexdigest()[:16],
                        "chunking_version": CHUNKING_VERSION,
                        "embedding_model": EMBED_MODEL,
                        "ingested_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    },
                }
            )
    return chunks


def write_preview(chunks, doc_id: str, suffix: str):
    out_dir = Path("knowledge/chunks")
    out_dir.mkdir(parents=True, exist_ok=True)
    md = out_dir / f"{doc_id}{suffix}.chunks.md"
    jl = out_dir / f"{doc_id}{suffix}.chunks.jsonl"
    with md.open("w", encoding="utf-8") as f:
        for n, c in enumerate(chunks, 1):
            m = c["metadata"]
            f.write(f"<!-- chunk {n} | {m['tokens']} tokens | part {m['part']}/{m['parts']} -->\n")
            f.write(c["content"] + "\n\n---\n\n")
    with jl.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    return md


# ---------- Loading ----------

def load(chunks, doc_id: str, chapter: str | None):
    print(f"Embedding {len(chunks)} chunks with {EMBED_MODEL}...")
    vectors = embed([c["content"] for c in chunks])

    from psycopg.types.json import Json

    with get_conn() as conn, conn.cursor() as cur:
        # replace previous chunks of this manual (or chapter), in one transaction
        sql = "DELETE FROM vector_store WHERE metadata->>'source' = 'manual' AND metadata->>'doc_id' = %s"
        params = [doc_id]
        if chapter:
            sql += " AND lower(metadata->>'chapter') = lower(%s)"
            params.append(chapter)
        cur.execute(sql, params)
        print(f"Removed {cur.rowcount} old chunks.")
        cur.executemany(
            "INSERT INTO vector_store (id, content, metadata, embedding) VALUES (%s, %s, %s, %s::vector)",
            [(c["id"], c["content"], Json(c["metadata"]), to_pgvector(v)) for c, v in zip(chunks, vectors)],
        )
    print(f"Inserted {len(chunks)} chunks.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manual", type=Path)
    ap.add_argument("--chapter")
    ap.add_argument("--max-tokens", type=int, default=500)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    chunks = build_chunks(args.manual, args.max_tokens, args.chapter)
    if not chunks:
        _, text = read_manual(args.manual)
        chapters = sorted({p[0] for p, _, _ in split_sections(text)})
        raise SystemExit(f"No chunks found. Chapters in this file: {', '.join(chapters)}")

    suffix = f".{slug(args.chapter)}" if args.chapter else ""
    preview = write_preview(chunks, args.manual.stem, suffix)
    sizes = [c["metadata"]["tokens"] for c in chunks]
    print(f"{len(chunks)} chunks | tokens min {min(sizes)}, median {sorted(sizes)[len(sizes)//2]}, max {max(sizes)}")
    print(f"Preview: {preview}")

    if not args.dry_run:
        load(chunks, args.manual.stem, args.chapter)


if __name__ == "__main__":
    main()
