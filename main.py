"""
main.py

Entry point for the Customer Complaint Chatbot.

Starts the Streamlit application and handles
user interaction with the RAG pipeline.

Author: Jaya Bharath
"""

import streamlit as st

from rag.rag_pipeline import RAGPipeline
from utils.config import PROJECT_NAME


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=PROJECT_NAME,
    page_icon="🤖",
    layout="wide",
)

# ==========================================================
# Load RAG Pipeline (Only Once)
# ==========================================================

@st.cache_resource
def load_chatbot():
    """
    Initialize the RAG pipeline once and cache it.
    """
    return RAGPipeline()


chatbot = load_chatbot()

# ==========================================================
# Session State
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================================
# Header
# ==========================================================

st.title("🤖 Customer Complaint Chatbot")

st.markdown(
    """
Ask questions related to:

- Orders
- Returns
- Customers
- Support Tickets
- Company Policies
"""
)

st.divider()

# ==========================================================
# Display Chat History
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================================
# Chat Input
# ==========================================================

question = st.chat_input("Ask your question...")

if question:

    # ---------------- User ---------------- #

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # ---------------- Assistant ---------------- #

    with st.chat_message("assistant"):

        with st.spinner("Searching knowledge base..."):

            response = chatbot.ask(question)

            st.markdown(response.answer)

            # Processing Time

            st.caption(
                f"⏱ Response Time : {response.processing_time:.2f} sec"
            )

            # Sources

            if response.sources:

                with st.expander("📄 Sources"):

                    for source in response.sources:

                        st.write(
                            f"**{source['filename']}**"
                        )

                        if "score" in source:

                            st.write(
                                f"Similarity : {source['score']:.4f}"
                            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.answer
            }
        )