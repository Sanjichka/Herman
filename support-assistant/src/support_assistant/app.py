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

import streamlit as st
from ask import ask

st.set_page_config(page_title="Herman – Support Assistant", page_icon="🏥", layout="centered")
st.title("Herman – Support Assistant")
st.caption("Ask a question about the software. Answers are drawn from the product manual.")

if "history" not in st.session_state:
    st.session_state.history = []

for q, result in st.session_state.history:
    st.chat_message("user").write(q)
    with st.chat_message("assistant"):
        st.write(result["answer"])
        if not result["refused"] and result["chunks"]:
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
        st.write(result["answer"])
        if not result["refused"] and result["chunks"]:
            with st.expander(f"Sources ({len(result['chunks'])})"):
                for chunk in result["chunks"]:
                    path = " > ".join(chunk.get("section_path", [chunk.get("section_title", "")]))
                    st.write(f"**{path}** — score {chunk['score']:.2f}")
    st.session_state.history.append((question, result))
