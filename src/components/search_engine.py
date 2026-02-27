import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.logger.logger import logging
from src.exception import CustomException


class SearchEngine:
    """
    Performs semantic search using TF-IDF + Cosine Similarity
    """

    def __init__(self, index: dict):
        self.vectorizer = index["vectorizer"]
        self.tfidf_matrix = index["matrix"]
        self.documents = index["documents"]

    def search(self, query: str, top_k: int = 5):
        try:
            logging.info(f"Searching for query: {query}")

            # 1️⃣ Transform query into vector
            query_vector = self.vectorizer.transform([query])

            # 2️⃣ Compute cosine similarity
            similarity_scores = cosine_similarity(
                query_vector,
                self.tfidf_matrix
            ).flatten()

            # 3️⃣ Get top K indices
            top_indices = np.argsort(similarity_scores)[::-1][:top_k]

            results = []

            for idx in top_indices:
                results.append({
                    "verse_id": self.documents[idx]["verse_id"],
                    "content": self.documents[idx]["content"],
                    "score": float(similarity_scores[idx])
                })

            logging.info("Search completed successfully.")
            return results

        except Exception as e:
            logging.error("Error during search.")
            raise CustomException(e, sys)