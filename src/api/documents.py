from fastapi import APIRouter

from models.documents import AddDocumentRequest
from milvus.document import insert_document
from services.bm25_service import rebuild_index

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/")
def add_document(request: AddDocumentRequest):
    result = insert_document(
        collection_name=request.collection_name,
        text=request.text,
    )

    rebuild_index()

    return {
        "status": "success",
        "insert_count": result["insert_count"],
        "ids": result["ids"],
    }