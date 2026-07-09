from fastapi import APIRouter

from milvus.document import insert_document
from services.bm25_service import rebuild_index

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/")
def add_document(
    collection_name: str,
    text: str,
):
    result = insert_document(
        collection_name=collection_name,
        text=text,
    )

    rebuild_index()

    return {
        "status": "success",
        "insert_count": result["insert_count"],
        "ids": result["ids"],
    }