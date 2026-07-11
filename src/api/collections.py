from fastapi import APIRouter

from milvus.collection import (
    create_collection,
    list_collections
)

router = APIRouter(
    prefix="/collections",
    tags=["Collections"]
)

@router.post("/{collection_name}")
def create(collection_name: str):
    create_collection(collection_name)
    return {
        "message": "Collection created"
    }

@router.get("/")
def list_all():
    return list_collections()