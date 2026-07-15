from fastapi import APIRouter

from models.collection import CreateCollectionRequest

from milvus.collection import (
    create_collection,
    list_collections,
)

router = APIRouter(
    prefix="/collections",
    tags=["Collections"],
)


@router.post("/")
def create(
    request: CreateCollectionRequest,
):
    create_collection(
        request.collection_name
    )

    return {
        "message": "Collection created"
    }


@router.get("/")
def list_all():
    return list_collections()