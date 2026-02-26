
import pdfplumber
from src.logger.logger import logging
from src.exception import CustomException
import sys


class PDFLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        """
        Extract text from PDF file.
        Returns full combined text.
        """
        try:
            logging.info("Opening PDF file.")

            full_text = ""

            with pdfplumber.open(self.file_path) as pdf:
                for page_number, page in enumerate(pdf.pages):
                    text = page.extract_text()

                    if text:
                        logging.info(f"Extracted text from page {page_number + 1}")
                        full_text += text + "\n"

            logging.info("PDF extraction completed successfully.")
            return full_text

        except Exception as e:
            logging.error("Error occurred during PDF extraction.")
            raise CustomException(e, sys)
