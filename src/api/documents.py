from fastapi import APIRouter
from milvus.document import insert_document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post("/")
def add_document(collection_name: str, text: str):
    return insert_document(
        collection_name=collection_name,
        text=text
    )