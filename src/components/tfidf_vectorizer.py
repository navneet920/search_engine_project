
import os
import pickle
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from src.logger.logger import logging
from src.exception import CustomException


class TFIDFVectorizer:

    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=(1, 3),   # unigrams + bigrams
            stop_words="english"
        )
        self.tfidf_matrix = None

    def fit_transform(self, documents: list):
        """
        Fit TF-IDF on cleaned documents
        """
        try:
            logging.info("Fitting TF-IDF vectorizer...")
            self.tfidf_matrix = self.vectorizer.fit_transform(documents)
            logging.info("TF-IDF fitting completed.")
            return self.tfidf_matrix

        except Exception as e:
            logging.error("Error during TF-IDF fitting.")
            raise CustomException(e, sys)

    def transform(self, query: str):
        """
        Transform search query into vector
        """
        return self.vectorizer.transform([query])

    def save(self, artifacts_path="artifacts"):
        """
        Save vectorizer and matrix
        """
        try:
            os.makedirs(artifacts_path, exist_ok=True)

            with open(os.path.join(artifacts_path, "vectorizer.pkl"), "wb") as f:
                pickle.dump(self.vectorizer, f)

            with open(os.path.join(artifacts_path, "tfidf_matrix.pkl"), "wb") as f:
                pickle.dump(self.tfidf_matrix, f)

            logging.info("TF-IDF artifacts saved successfully.")

        except Exception as e:
            logging.error("Error saving TF-IDF artifacts.")
            raise CustomException(e, sys)

    @staticmethod
    def load(artifacts_path="artifacts"):
        """
        Load saved vectorizer and matrix
        """
        with open(os.path.join(artifacts_path, "vectorizer.pkl"), "rb") as f:
            vectorizer = pickle.load(f)

        with open(os.path.join(artifacts_path, "tfidf_matrix.pkl"), "rb") as f:
            matrix = pickle.load(f)

        return vectorizer, matrix