import os
import pickle
import sys
import numpy as np
from sentence_transformers import SentenceTransformer
from src.logger.logger import logging
from src.exception import CustomException
from src.config.configuration import config

class EmbeddingModel:
    """
    Semantic embedding model using Sentence Transformers
    """

    def __init__(self, model_name=None):
        self.model_name=config.EMBEDDING_MODEL_NAME
        self.model = SentenceTransformer(self.model_name)
        # Load model with optional HuggingFace token
        self.model = SentenceTransformer(
            self.model_name,
            token=config.HF_TOKEN
        )
        self.embeddings = None

    def encode_documents(self, documents: list):
        try:
            logging.info("Generating document embeddings...")
            self.embeddings = self.model.encode(
                documents,
                convert_to_numpy=True,
                show_progress_bar=True
            )
            logging.info("Embeddings generated successfully.")
            return self.embeddings

        except Exception as e:
            raise CustomException(e, sys)

    def encode_query(self, query: str):
        return self.model.encode([query], convert_to_numpy=True)

    def save(self, artifacts_path=None):
        artifacts_path =config.ARTIFACTS_PATH
        os.makedirs(artifacts_path, exist_ok=True)

        with open(os.path.join(artifacts_path, "embeddings.pkl"), "wb") as f:
            pickle.dump(self.embeddings, f)

    @staticmethod
    def load(artifacts_path=None):
        artifacts_path =config.ARTIFACTS_PATH
        with open(os.path.join(artifacts_path, "embeddings.pkl"), "rb") as f:
            embeddings = pickle.load(f)

        return embeddings