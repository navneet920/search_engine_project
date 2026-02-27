from src.components.search_engine import SearchEngine
from src.components.semantic_search_engine import SemanticSearchEngine
from src.components.hybrid_search_engine import HybridSearchEngine
from src.components.index_builder import IndexBuilder
from src.components.preprocessor import Preprocessor


class SearchPipeline:

    def __init__(self, mode="hybrid", artifacts_path="artifacts"):
        """
        mode:
            - "tfidf"
            - "semantic"
            - "hybrid"
        """

        self.mode = mode

        if mode == "tfidf":
            builder = IndexBuilder(artifacts_path)
            index = builder.build()
            self.engine = SearchEngine(index)

        elif mode == "semantic":
            self.engine = SemanticSearchEngine(artifacts_path)

        elif mode == "hybrid":
            self.engine = HybridSearchEngine(artifacts_path, alpha=0.5)

        else:
            raise ValueError("Invalid mode. Choose: tfidf, semantic, hybrid")

    def run(self, query: str, top_k: int = 5):

        # Clean query once here
        query = Preprocessor().clean_text(query)

        results = self.engine.search(query, top_k=top_k)

        return results