from src.components.semantic_search_engine import SemanticSearchEngine


if __name__ == "__main__":

    engine = SemanticSearchEngine()

    results = engine.search("what is karma", top_k=3)

    for r in results:
        print("\nVerse:", r["verse_id"])
        print("Score:", round(r["score"], 4))
        print(r["content"])
