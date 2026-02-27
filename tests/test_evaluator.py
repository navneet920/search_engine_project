from src.components.index_builder import IndexBuilder
from src.components.search_engine import SearchEngine
from src.components.evaluator import Evaluator


if __name__ == "__main__":

    builder = IndexBuilder()
    index = builder.build()

    engine = SearchEngine(index)

    query = "duty"

    # Ground truth (manually defined)
    relevant_docs = ["2.47", "3.19", "18.47"]

    results = engine.search(query, top_k=10)

    precision = Evaluator.precision_at_k(results, relevant_docs, k=5)
    recall = Evaluator.recall_at_k(results, relevant_docs, k=5)
    mrr = Evaluator.mean_reciprocal_rank(results, relevant_docs)

    print("Precision@5:", round(precision, 4))
    print("Recall@5:", round(recall, 4))
    print("MRR:", round(mrr, 4))