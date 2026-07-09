from fastapi import APIRouter

from models.rag import (
    RAGRequest,
    RAGResponse
)

from services.rag_service import ask_question

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

@router.post("/ask", response_model=RAGResponse)
def rag(request: RAGRequest):
    result = ask_question(
        collection_name=request.collection_name,
        question=request.question
    )

    return result