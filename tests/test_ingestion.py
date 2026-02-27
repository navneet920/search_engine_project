from src.pipeline.ingestion_pipeline import IngestionPipeline


if __name__ == "__main__":

    pdf_path = "data/raw/geeta.pdf"

    pipeline = IngestionPipeline(pdf_path)
    chunks = pipeline.run()

    print("Total verses:", len(chunks))

    if chunks:
        print("First verse:")
        print(chunks[0])