from src.pipeline.search_pipeline import SearchPipeline
from src.components.evaluator import Evaluator


if __name__ == "__main__":

    pipeline = SearchPipeline(mode="hybrid")

    evaluator = Evaluator(pipeline)

    ground_truth = {
        "duty and righteousness": ["18.30", "18.31"],
        "self knowledge": ["9.01"]
    }

    metrics = evaluator.evaluate(ground_truth, top_k=5)

    print(metrics)