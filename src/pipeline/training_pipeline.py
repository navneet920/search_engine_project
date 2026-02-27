from src.utils.storage import Storage
from src.components.tfidf_vectorizer import TFIDFVectorizer
from src.logger.logger import logging


class TrainingPipeline:

    def run(self):
        logging.info("========== Training Pipeline Started ==========")

        # Load cleaned chunks
        chunks = Storage.load_chunks()

        documents = [chunk["clean_content"] for chunk in chunks]

        # Train TF-IDF
        vectorizer = TFIDFVectorizer()
        vectorizer.fit_transform(documents)

        # Save artifacts
        vectorizer.save()

        logging.info("========== Training Pipeline Completed ==========")