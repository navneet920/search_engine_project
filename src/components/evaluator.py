import numpy as np

from src.config.configuration import config
class Evaluator:

    def __init__(self, pipeline,top_k=None):
        """
        pipeline = SearchPipeline instance
        """
        self.pipeline = pipeline
        self.top_k=config.DEFAULT_TOP_K

    def evaluate(self, ground_truth, top_k=None):
        top_k=self.top_k
        precision_scores = []
        recall_scores = []
        reciprocal_ranks = []

        for query, relevant_docs in ground_truth.items():

            results = self.pipeline.run(query, top_k=top_k)

            retrieved_ids = [r["verse_id"] for r in results]

            # --- Precision@K ---
            relevant_retrieved = [
                doc for doc in retrieved_ids if doc in relevant_docs
            ]

            precision = len(relevant_retrieved) / top_k
            precision_scores.append(precision)

            # --- Recall@K ---
            recall = len(relevant_retrieved) / len(relevant_docs)
            recall_scores.append(recall)

            # --- MRR ---
            rr = 0
            for rank, doc_id in enumerate(retrieved_ids):
                if doc_id in relevant_docs:
                    rr = 1 / (rank + 1)
                    break

            reciprocal_ranks.append(rr)

        return {
            "Precision@{}".format(top_k): np.mean(precision_scores),
            "Recall@{}".format(top_k): np.mean(recall_scores),
            "MRR": np.mean(reciprocal_ranks)
        }