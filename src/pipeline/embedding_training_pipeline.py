from src.utils.storage import Storage
from src.components.embedding_model import EmbeddingModel


class EmbeddingTrainingPipeline:

    def run(self):
        chunks = Storage.load_chunks()

        documents = [chunk["content"] for chunk in chunks]

        model = EmbeddingModel()
        model.encode_documents(documents)
        model.save()

        print("Embeddings training completed.")