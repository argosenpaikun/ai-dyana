from datetime import datetime

from mongodb.client import get_mongodb


COLLECTION_NAME = "documents"


def insert_document_metadata(
    milvus_id: int,
    text: str,
):
    """
    Store document metadata in MongoDB.
    """
    database = get_mongodb()

    result = database[COLLECTION_NAME].insert_one(
        {
            "milvus_id": milvus_id,
            "text": text,
            "created_at": datetime.utcnow(),
        }
    )

    return str(result.inserted_id)


def get_document_metadata(
    milvus_id: int,
):
    """
    Retrieve document metadata by Milvus ID.
    """
    database = get_mongodb()

    return database[COLLECTION_NAME].find_one(
        {
            "milvus_id": milvus_id,
        },
        {
            "_id": 0,
        },
    )


def delete_document_metadata(
    milvus_id: int,
):
    """
    Delete document metadata by Milvus ID.
    """
    database = get_mongodb()

    database[COLLECTION_NAME].delete_one(
        {
            "milvus_id": milvus_id,
        }
    )


def get_all_document_metadata():
    """
    Return all document metadata.
    """
    database = get_mongodb()

    return list(
        database[COLLECTION_NAME].find(
            {},
            {
                "_id": 0,
            },
        )
    )