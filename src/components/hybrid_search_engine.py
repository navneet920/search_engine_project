import os
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from src.components.index_builder import IndexBuilder
from src.components.embedding_model import EmbeddingModel
from src.components.preprocessor import Preprocessor
from src.config.configuration import config

class HybridSearchEngine:

    def __init__(self, artifacts_path=None, alpha=None):
        """
        alpha: weight for TF-IDF
        (1 - alpha): weight for embeddings
        """

        self.alpha = config.HYBRID_ALPHA
        self.artifacts_path=config.ARTIFACTS_PATH

        # ---- Load TF-IDF index ----
        builder = IndexBuilder(self.artifacts_path)
        index = builder.build()

        self.vectorizer = index["vectorizer"]
        self.tfidf_matrix = index["matrix"]
        self.documents = index["documents"]

        # ---- Load embeddings ----
        embeddings_path = os.path.join(self.artifacts_path, "embeddings.pkl")

        if not os.path.exists(embeddings_path):
            raise FileNotFoundError(
                "embeddings.pkl not found. Run EmbeddingTrainingPipeline first."
            )

        with open(embeddings_path, "rb") as f:
            self.embeddings = pickle.load(f)

        self.embedding_model = EmbeddingModel()

    def search(self, query: str, top_k: int = 5):

        query = Preprocessor().clean_text(query)

        # -------- TF-IDF Similarity --------
        tfidf_query = self.vectorizer.transform([query])
        tfidf_scores = cosine_similarity(
            tfidf_query,
            self.tfidf_matrix
        ).flatten()

        # -------- Embedding Similarity --------
        query_embedding = self.embedding_model.encode_query(query)
        embedding_scores = cosine_similarity(
            query_embedding,
            self.embeddings
        ).flatten()

        # -------- Normalize Scores --------
        tfidf_scores = self._normalize(tfidf_scores)
        embedding_scores = self._normalize(embedding_scores)

        # -------- Combine --------
        hybrid_scores = (
            self.alpha * tfidf_scores +
            (1 - self.alpha) * embedding_scores
        )

        # -------- Top Results --------
        top_indices = np.argsort(hybrid_scores)[::-1][:top_k]

        results = []

        for idx in top_indices:
            results.append({
                "verse_id": self.documents[idx]["verse_id"],
                "content": self.documents[idx]["content"],
                "score": float(hybrid_scores[idx])
            })

        return results

    @staticmethod
    def _normalize(scores):
        min_score = np.min(scores)
        max_score = np.max(scores)

        if max_score - min_score == 0:
            return scores

        return (scores - min_score) / (max_score - min_score)