from fastapi import APIRouter, HTTPException, status

from models.documents import AddDocumentRequest
from models.documents import DeleteDocumentRequest
from milvus.document import insert_document, delete_document
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

@router.delete("/")
def remove_document(request: DeleteDocumentRequest):
    try:
        result = delete_document(
            collection_name=request.collection_name,
            document_id=request.document_id
        )

        rebuild_index()

        return {
            "status": "success",
            **result
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )