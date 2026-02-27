import os
import pickle
import sys
from src.utils.storage import Storage
from src.logger.logger import logging
from src.exception import CustomException


class IndexBuilder:
    """
    Builds searchable index from:
    - vectorizer.pkl
    - tfidf_matrix.pkl
    - chunks.json
    """

    def __init__(self, artifacts_path="artifacts"):
        self.artifacts_path = artifacts_path
        self.vectorizer = None
        self.tfidf_matrix = None
        self.documents = None

    def build(self):
        try:
            logging.info("========== Building Search Index ==========")

            # Load vectorizer
            with open(os.path.join(self.artifacts_path, "vectorizer.pkl"), "rb") as f:
                self.vectorizer = pickle.load(f)

            # Load TF-IDF matrix
            with open(os.path.join(self.artifacts_path, "tfidf_matrix.pkl"), "rb") as f:
                self.tfidf_matrix = pickle.load(f)

            # Load chunks metadata
            self.documents = Storage.load_chunks()

            logging.info("Index built successfully.")

            return {
                "vectorizer": self.vectorizer,
                "matrix": self.tfidf_matrix,
                "documents": self.documents
            }

        except Exception as e:
            logging.error("Error building index.")
            raise CustomException(e, sys)