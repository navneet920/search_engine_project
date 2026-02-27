from pydantic import BaseModel

class SearchResponse(BaseModel):
    content:str
