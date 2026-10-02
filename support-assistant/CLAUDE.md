# Support Assistant

## What this is

A standalone prototype of a client support assistant for medical software. It answers questions about how the software works, drawing only from two sources: the product manual and a history of real client support questions. It cites the manual section behind every answer. When a question falls outside what it has, it says so and routes the person to a human — it never guesses.

A confident wrong answer is worse than no answer. That refusal behaviour is a core feature.

## Data sources

- **Product manual** — documents how the software works.
- **Support question history** — real client questions and answers.

Search both sources for every question. Every answer must cite where it draws from.

## What matters vs. what's throwaway

**Keep (these survive into production):**
- Knowledge files (manual chunks, support history)
- Retrieval logic (chunking, metadata, similarity threshold, query rewriting)
- Conversation and retrieval logs

**Throwaway:**
- The Streamlit UI (deleted when production UI is built)

## Tech stack

| Component | Choice |
|-----------|--------|
| Vector DB | Supabase Postgres + pgvector, EU region |
| Embeddings | `text-embedding-3-small`, 1536 dimensions |
| Generation | OpenAI (same client) |
| Prototype UI | Streamlit Community Cloud |
| Package manager | uv |
| Language | Python 3.13+ |

The embedding dimension (1536) matches Spring AI's expectations for the production migration.

## Build order

1. Script-based retrieval over one manual chapter + clients tickets history — no UI yet
2. Add similarity threshold (reject low-confidence matches) and query rewriting
3. Wrap in Streamlit
4. Ingest remaining manual chapters and support history

Don't build the next stage until the current one works on real questions.

## Ingestion

- Python batch job (stays a batch job in production too)
- Chunk the manual; attach metadata (section, chapter, page) to every chunk
- The chunking strategy and metadata schema are the main design decisions — treat them carefully

## Logging

Track per conversation:
- Messages
- Retrieval events (which chunks were returned, similarity scores)

Review weekly to find manual gaps and poorly written content.

## Production path (future, not now)

- Query path moves to Spring AI on production Postgres
- UI becomes a Vue component inside the medical portal
- Streamlit is deleted
- Ingestion stays a Python batch job

## Working style

The owner is not a developer. Time goes into the data (chunking, metadata, retrieval quality), not infrastructure. Keep code minimal and off-the-shelf. Own only the ingestion and retrieval logic.

When suggesting approaches, prefer simple and correct. Explain tradeoffs in terms of retrieval quality, not engineering elegance.