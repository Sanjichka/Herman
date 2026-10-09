"""
Herman – Support Assistant (Streamlit prototype UI)

Run:
    cd support-assistant
    uv run streamlit run src/support_assistant/app.py
"""

import sys
from pathlib import Path

# Make sibling modules importable when run directly by Streamlit
sys.path.insert(0, str(Path(__file__).parent))

import uuid

import streamlit as st
from ask import ask
from common import get_conn, log_conversation

st.set_page_config(page_title="Herman – Support Assistant", page_icon="🏥", layout="centered")
st.title("Herman – Support Assistant")
st.caption("Ask a question about the software. Answers are drawn from the product manual.")

if "history" not in st.session_state:
    st.session_state.history = []

if "conversation_id" not in st.session_state:
    conv_id = str(uuid.uuid4())
    st.session_state.conversation_id = conv_id
    try:
        with get_conn() as conn:
            conn.execute("INSERT INTO conversations (id) VALUES (%s::uuid)", (conv_id,))
            conn.commit()
    except Exception as exc:
        print(f"[session init] failed: {exc}")

for q, result in st.session_state.history:
    st.chat_message("user").write(q)
    with st.chat_message("assistant"):
        st.write(result["answer"])
        if result["chunks"]:
            with st.expander(f"Sources ({len(result['chunks'])})"):
                for chunk in result["chunks"]:
                    path = " > ".join(chunk.get("section_path", [chunk.get("section_title", "")]))
                    st.write(f"**{path}** — score {chunk['score']:.2f}")

question = st.chat_input("Ask a question about the software...")
if question:
    st.chat_message("user").write(question)
    with st.chat_message("assistant"):
        with st.spinner("Searching manual..."):
            result = ask(question)
        log_conversation(st.session_state.conversation_id, question, result)
        st.write(result["answer"])
        if result["chunks"]:
            with st.expander(f"Sources ({len(result['chunks'])})"):
                for chunk in result["chunks"]:
                    path = " > ".join(chunk.get("section_path", [chunk.get("section_title", "")]))
                    st.write(f"**{path}** — score {chunk['score']:.2f}")
    st.session_state.history.append((question, result))
