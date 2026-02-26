import os
from pathlib import Path
import logging

logging.basicConfig(format='[%(pastime)s]:%(message)s:')



list_of_files = [

    # GitHub workflow
    ".github/workflows/.gitkeep",

    # Source Code
    "src/__init__.py",
    "src/components/__init__.py",

    # Core Components
    "src/components/preprocessor.py",
    "src/components/document_chunker.py",      # 🔥 Needed for Geeta
    "src/components/index_builder.py",
    "src/components/tfidf_vectorizer.py",
    "src/components/search_engine.py",
    "src/components/evaluator.py",

    # Utilities
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/utils/file_io.py",

    # Logging
    "src/logger/__init__.py",
    "src/logger/logger.py",

    # Configuration
    "src/config/__init__.py",
    "src/config/configuration.py",

    # Pipeline
    "src/pipeline/__init__.py",
    "src/pipeline/ingestion_pipeline.py",   # 🔥 upload once
    "src/pipeline/search_pipeline.py",

    # Exception handling
    "src/exception.py",

    # Data folders
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",

    # Artifacts
    "artifacts/inverted_index.json",
    "artifacts/tfidf_matrix.pkl",
    "artifacts/vectorizer.pkl",
    "artifacts/metadata.json",  # 🔥 required to map chunk → verse

    # Tests
    "tests/__init__.py",
    "tests/test_index_builder.py",
    "tests/test_search_engine.py",
    "tests/test_chunking.py",

    # Config files
    "config/config.yaml",
    "params.yaml",

    # Main execution
    "main.py",

    # Project files
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",

    # Research notebook
    "research/search_engine_experiments.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file :{filepath}")

    else:
        logging.info(f"{filename} is already exists")