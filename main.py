import time
from fastapi import FastAPI, HTTPException
from typing import List

from src.schemas.user_query import SearchRequest
from src.schemas.response import SearchResponse
from src.pipeline.search_pipeline import SearchPipeline
from src.config.configuration import config
from src.logger.logger import logging


app = FastAPI(
    title="Bhagavad Gita Search Engine API",
    version="1.0.0",
    description="Hybrid Semantic + TF-IDF Search API"
)

# Load pipeline once at startup
pipeline = SearchPipeline(mode=config.SEARCH_MODE)


@app.get("/")
def home():
    return {"message": "Welcome to Bhagavad Gita Search Engine 🚀"}


@app.post("/search", response_model=List[SearchResponse])
def search(request: SearchRequest):

    start_time = time.time()

    try:
        results = pipeline.run(
            query=request.query,
            top_k=2  # Force only top 2 results
        )

        if not results:
            raise HTTPException(
                status_code=404,
                detail="No results found"
            )

        response_time = round(time.time() - start_time, 4)

        logging.info(f"Query: {request.query}")
        logging.info(f"Results returned: {len(results)}")
        logging.info(f"Response time: {response_time} seconds")

        return [
            SearchResponse(content=r["content"])
            for r in results
        ]

    except Exception as e:
        logging.error("Search endpoint failed.")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )