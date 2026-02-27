import os


class Config:

    def __init__(self):

        # -------- Paths --------
        self.BASE_DIR = os.getcwd()
        self.ARTIFACTS_PATH = os.path.join(self.BASE_DIR, "artifacts")

        # -------- Search --------
        self.DEFAULT_TOP_K = 5
        self.SEARCH_MODE = "hybrid"   # tfidf | semantic | hybrid
        self.HYBRID_ALPHA = 0.5

        # -------- Embeddings --------
        self.EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

        # -------- Evaluation --------
        self.EVAL_TOP_K = 5


# Global config object
config = Config()