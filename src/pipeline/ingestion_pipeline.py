import sys
from src.components.pdf_loader import PDFLoader
from src.components.document_chunker import Chunker
from src.components.preprocessor import Preprocessor
from src.utils.storage import Storage
from src.logger.logger import logging
from src.exception import CustomException


class IngestionPipeline:
    """
    Ingestion Pipeline:
    1. Extract text from PDF
    2. Chunk text by verse
    3. Apply advanced preprocessing
    4. Save structured chunks to artifacts
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.loader = PDFLoader(pdf_path)
        self.chunker = Chunker()
        self.preprocessor = Preprocessor()

    def run(self):
        try:
            logging.info("========== Ingestion Pipeline Started ==========")

            # Step 1: Extract text
            raw_text = self.loader.extract_text()

            if not raw_text or len(raw_text.strip()) == 0:
                raise ValueError("Extracted PDF text is empty.")

            logging.info("PDF extraction completed successfully.")

            # Step 2: Chunk by verse
            chunks = self.chunker.chunk_by_verse(raw_text)

            if not chunks:
                raise ValueError("No verses detected during chunking.")

            logging.info(f"Total verses chunked: {len(chunks)}")

            # Step 3: Advanced preprocessing
            for chunk in chunks:
                chunk["clean_content"] = self.preprocessor.clean_text(
                    chunk["content"]
                )

            logging.info("Advanced preprocessing applied to all verses.")

            # Step 4: Save artifacts
            Storage.save_chunks(chunks)

            logging.info("Chunks saved at artifacts/chunks.json")
            logging.info("========== Ingestion Pipeline Completed ==========")

            return chunks

        except Exception as e:
            logging.error("Error occurred in Ingestion Pipeline.")
            raise CustomException(e, sys)