"""Shared settings and helpers for ingestion, search and evaluation."""

import os

from dotenv import load_dotenv

load_dotenv()

# Must match the vector_store table (vector(1536)) and the future Spring AI config.
EMBED_MODEL = "text-embedding-3-small"
EMBED_DIMENSIONS = 1536
EMBED_BATCH = 100

# Bump this whenever you change how chunks are made, so eval runs can be compared.
CHUNKING_VERSION = "v1-headings-500"


def _parse_db_url(url: str) -> dict:
    """Parse a postgres:// URL whose password may contain special chars like [], %+."""
    from urllib.parse import unquote
    # strip scheme
    rest = url.split("://", 1)[1]
    # split userinfo from host at the LAST '@' (password may contain '@')
    at = rest.rfind("@")
    userinfo, hostpart = rest[:at], rest[at + 1:]
    # split user:password at the FIRST ':'
    colon = userinfo.index(":")
    user = unquote(userinfo[:colon])
    password = unquote(userinfo[colon + 1:])
    # split host/port from dbname
    slash = hostpart.index("/")
    hostport, dbname = hostpart[:slash], hostpart[slash + 1:]
    # split host:port at the LAST ':'
    last_colon = hostport.rfind(":")
    host = hostport[:last_colon]
    port = int(hostport[last_colon + 1:])
    return dict(host=host, port=port, dbname=dbname, user=user, password=password)


def get_conn():
    import psycopg

    url = os.environ.get("DATABASE_URL")
    if not url:
        raise SystemExit("DATABASE_URL is missing from .env")
    conn = psycopg.connect(**_parse_db_url(url))
    # Supabase keeps the vector type in the 'extensions' schema; harmless elsewhere.
    conn.execute("SET search_path TO public, extensions")
    return conn


def embed(texts: list[str]) -> list[list[float]]:
    from openai import OpenAI

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is missing from .env")
    client = OpenAI()
    vectors = []
    for i in range(0, len(texts), EMBED_BATCH):
        batch = texts[i : i + EMBED_BATCH]
        resp = client.embeddings.create(model=EMBED_MODEL, input=batch, dimensions=EMBED_DIMENSIONS)
        vectors.extend(d.embedding for d in resp.data)
    return vectors


def to_pgvector(vec: list[float]) -> str:
    """Format a vector as pgvector text, so no extra adapter is needed."""
    return "[" + ",".join(f"{x:.7f}" for x in vec) + "]"


try:
    import tiktoken
    _enc = tiktoken.get_encoding("cl100k_base")
except Exception:
    _enc = None


def n_tokens(text: str) -> int:
    return len(_enc.encode(text)) if _enc else len(text) // 4
