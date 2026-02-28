import streamlit as st
import requests
import re

API_URL = "http://127.0.0.1:8000/search"

st.set_page_config(
    page_title="Bhagavad Gita AI",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Bhagavad Gita AI")

# Chat input (no history stored)
if prompt := st.chat_input("Ask something about Bhagavad Gita..."):

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"query": prompt},

                )

                if response.status_code == 200:
                    results = response.json()

                    if results:
                        for i, r in enumerate(results, 1):
                            clean_text=re.sub(r'[()]','',r["content"])
                            st.write(clean_text)
                            st.divider()
                    else:
                        st.write("No relevant verses found.")

                else:
                    st.write("API error occurred.")

            except Exception as e:
                st.write(f"Connection error: {e}")