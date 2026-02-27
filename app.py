import streamlit as st
import requests

# 🔗 Change this if deploying backend
API_URL = "http://127.0.0.1:8000/search"

st.set_page_config(
    page_title="Bhagavad Gita Search",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Bhagavad Gita Semantic Search")
st.markdown("Ask any question related to the Bhagavad Gita.")

query = st.text_input("Enter your question:")

if st.button("Search"):

    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Searching..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"query": query},
                    timeout=10
                )

                if response.status_code == 200:
                    results = response.json()

                    if not results:
                        st.info("No results found.")
                    else:
                        st.success("Top 2 Results:")
                        st.balloons()

                        for i, result in enumerate(results, 1):
                            with st.container():
                                st.markdown(f"### 🔎 Result {i}")
                                st.info(result["content"])
                                st.divider()

                else:
                    st.error(f"API Error: {response.json().get('detail')}")

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to backend. Make sure FastAPI is running.")

            except Exception as e:
                st.error("Something went wrong.")