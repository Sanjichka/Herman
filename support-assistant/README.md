# Support Assistant

A prototype client support assistant for medical software. It answers questions about how the software works by searching a product manual and a history of real support questions — and cites the manual section behind every answer.

When a question falls outside what it knows, it says so and routes to a human. It never guesses.

## Stack

- **Vector DB:** Supabase Postgres + pgvector (EU region)
- **Embeddings:** `text-embedding-3-small` (1536 dimensions)
- **Generation:** OpenAI
- **UI:** Streamlit (prototype only — replaced in production)
- **Language:** Python 3.13+, managed with `uv`
