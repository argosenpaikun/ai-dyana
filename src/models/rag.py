from pydantic import BaseModel

class RAGRequest(BaseModel):
    question: str
    collection_name: str

class RAGResponse(BaseModel):
    answer: str
    sources: list