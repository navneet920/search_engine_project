from src.components.index_builder import IndexBuilder


if __name__ == "__main__":
    builder = IndexBuilder()
    index = builder.build()

    print("Vectorizer loaded:", type(index["vectorizer"]))
    print("Matrix shape:", index["matrix"].shape)
    print("Total documents:", len(index["documents"]))