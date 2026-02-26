import sys

from src.components.document_chunker import Chunker
from src.components.pdf_loader import PDFLoader
from src.logger.logger import logging
from src.exception import CustomException


def run_chunking_pipeline(pdf_path: str):

    try:
        logging.info("Chunking pipeline started.")

        # Step 1: Extract text
        loader = PDFLoader(pdf_path)
        raw_text = loader.extract_text()
        logging.info("PDF text extraction completed.")

        # Step 2: Chunk by verse
        chunker = Chunker()
        chunks = chunker.chunk_by_verse(raw_text)
        logging.info(f"Total verses extracted: {len(chunks)}")

        logging.info("Chunking pipeline completed successfully.")
        return chunks

    except Exception as e:
        logging.error("Error in chunking pipeline.")
        raise CustomException(e, sys)

if __name__ == "__main__":

    pdf_path = "data/raw/geeta.pdf"

    chunks = run_chunking_pipeline(pdf_path)

    print("Total verses:", len(chunks))

    if chunks:
        print("First verse:")
        print(chunks[0])