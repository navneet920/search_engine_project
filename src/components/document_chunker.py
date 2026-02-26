import re
from src.logger.logger import logging
from src.exception import CustomException
import sys


class Chunker:
    def __init__(self):
        pass

    def chunk_by_verse(self, text: str):
        """
        Splits text based on verse pattern like:
        12.11
        13.01
        2.47

        Returns:
        [
            {"verse_id": "12.11", "content": "..."},
            ...
        ]
        """

        try:
            logging.info("Starting verse-based chunking.")

            # 🔹 Regex pattern for verse numbers
            # Matches patterns like 1.1, 12.11, 18.66 etc.
            pattern = r'\b(\d{1,2}\.\d{1,3})\b'

            parts = re.split(pattern, text)

            chunks = []

            # parts format:
            # [text_before, verse_id, verse_text, verse_id, verse_text...]

            for i in range(1, len(parts), 2):

                verse_id = parts[i]
                verse_text = parts[i + 1].strip()

                # Remove extra whitespace
                verse_text = re.sub(r'\s+', ' ', verse_text)

                # Filter very small garbage chunks
                if len(verse_text) > 40:
                    chunks.append({
                        "verse_id": verse_id,
                        "content": verse_text
                    })

            logging.info(f"Total verses chunked: {len(chunks)}")

            return chunks

        except Exception as e:
            logging.error("Error during verse chunking.")
            raise CustomException(e, sys)