from fastapi import APIRouter

from mongodb.document import get_all_document_metadata

router = APIRouter(
    prefix="/mongodb",
    tags=["MongoDB"],
)


@router.get("/documents")
def get_documents():
    return get_all_document_metadata()