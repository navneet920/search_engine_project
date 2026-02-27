from src.components.hybrid_search_engine import HybridSearchEngine

if __name__ == "__main__":

    engine = HybridSearchEngine(alpha=0.5)

    query = "what is karma"

    results = engine.search(query, top_k=5)

    for r in results:
        print("\nVerse:", r["verse_id"])
        print("Score:", round(r["score"], 4))
        print(r["content"])