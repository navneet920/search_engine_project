from src.pipeline.search_pipeline import SearchPipeline

if __name__ == "__main__":

    # Change mode here
    pipeline = SearchPipeline(mode="hybrid")

    query = "what is karma"

    results = pipeline.run(query, top_k=5)

    for r in results:
        print("\nVerse:", r["verse_id"])
        print("Score:", round(r["score"], 4))
        print(r["content"])