import streamlit as st

from src.services.search_service import SearchService


st.set_page_config(
    page_title="Semantic Search",
    page_icon="🔎",
    layout="wide",
)


@st.cache_resource
def get_search_service():
    return SearchService()


def main():
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 18px;
            color: #777;
            margin-bottom: 30px;
        }

        .result-card {
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #ddd;
            margin-bottom: 15px;
        }

        .score {
            font-size: 14px;
            color: #666;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-title">🔎 Semantic Search Engine</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="subtitle">'
        "Search documents by meaning, not just exact keywords."
        "</div>",
        unsafe_allow_html=True,
    )

    query = st.text_input(
        "Search",
        placeholder="Try: routing protocols, network loops, Python...",
        label_visibility="collapsed",
    )

    st.divider()

    if not query:
        st.info("Enter a query above to start searching.")
        return

    with st.spinner("Searching..."):
        search_service = get_search_service()
        results = search_service.search(query)

    st.subheader(f"Top {len(results)} Results")

    for index, result in enumerate(results, start=1):
        st.markdown(
            f"""
            <div class="result-card">
                <h4>{index}. Result</h4>
                <p>{result["document"]}</p>
                <div class="score">
                    Similarity Score: {result["score"]:.4f}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()