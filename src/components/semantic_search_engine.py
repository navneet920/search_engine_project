import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.components.embedding_model import EmbeddingModel
from src.utils.storage import Storage
from src.logger.logger import logging
from src.config.configuration import config


class SemanticSearchEngine:

    def __init__(self, artifacts_path=None,top_k=None):
        self.artifacts_path=config.ARTIFACTS_PATH
        self.top_k = config.DEFAULT_TOP_K
        self.documents = Storage.load_chunks()
        self.embeddings = EmbeddingModel.load()
        logging.info("Embedding model load")
        self.model = EmbeddingModel()  # loads transformer

    def search(self, query: str, top_k=None):
        top_k=self.top_k
        query_embedding = self.model.encode_query(query)

        similarity_scores = cosine_similarity(
            query_embedding,
            self.embeddings
        ).flatten()

        top_indices = np.argsort(similarity_scores)[::-1][:top_k]

        results = []

        for idx in top_indices:
            results.append({
                "verse_id": self.documents[idx]["verse_id"],
                "content": self.documents[idx]["content"],
                "score": float(similarity_scores[idx])
            })
        logging.info("Successfully compute the results")
        return results