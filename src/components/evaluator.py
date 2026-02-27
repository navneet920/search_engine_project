import numpy as np


class Evaluator:
    """
    Evaluates search results using:
    - Precision@K
    - Recall@K
    - MRR
    """

    @staticmethod
    def precision_at_k(results, relevant_docs, k):
        """
        results: list of search result dicts
        relevant_docs: list of relevant verse_ids
        """
        retrieved_k = results[:k]
        retrieved_ids = [r["verse_id"] for r in retrieved_k]

        relevant_retrieved = len(set(retrieved_ids) & set(relevant_docs))

        return relevant_retrieved / k

    @staticmethod
    def recall_at_k(results, relevant_docs, k):
        retrieved_k = results[:k]
        retrieved_ids = [r["verse_id"] for r in retrieved_k]

        relevant_retrieved = len(set(retrieved_ids) & set(relevant_docs))

        return relevant_retrieved / len(relevant_docs)

    @staticmethod
    def mean_reciprocal_rank(results, relevant_docs):
        """
        MRR = 1 / rank of first relevant document
        """
        for idx, result in enumerate(results):
            if result["verse_id"] in relevant_docs:
                return 1 / (idx + 1)

        return 0.0