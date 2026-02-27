from src.components.index_builder import IndexBuilder
from src.components.search_engine import SearchEngine
from src.components.preprocessor import Preprocessor


if __name__ == "__main__":

    # Build index
    builder = IndexBuilder()
    index = builder.build()
    preprocessor = Preprocessor()
    # Initialize search engine
    engine = SearchEngine(index)
    query="duty and righteousness"

    query = preprocessor.clean_text(query)
    print(query)
    # Run search
    results = engine.search(query, top_k=3)


    for r in results:
        print(f"\nVerse: {r['verse_id']}")
        print(f"Score: {r['score']:.4f}")
        print(r["content"])