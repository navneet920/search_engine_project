from pydantic import BaseModel,Field,field_validator
from typing import Annotated


class SearchRequest(BaseModel):
    query:Annotated[str,Field(...,min_length=3,max_length=300,description="User search query (3-300 characters)")]


@field_validator("query")
def validate_query(cls, value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError("Query cannot be empty or whitespace")
    return value