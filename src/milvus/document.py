from milvus.client import get_milvus_client
from milvus.embedding import generate_embedding

from mongodb.document import (
    insert_document_metadata,
)


def insert_document(
    collection_name: str,
    text: str,
):
    """
    Insert a document into Milvus and MongoDB.
    """
    client = get_milvus_client()

    embedding = generate_embedding(text)

    data = [
        {
            "text": text,
            "vector": embedding,
        }
    ]

    result = client.insert(
        collection_name=collection_name,
        data=data,
    )

    milvus_id = result["ids"][0]

    insert_document_metadata(
        milvus_id=milvus_id,
        text=text,
    )

    print("Document inserted successfully.")

    return {
        "insert_count": result["insert_count"],
        "ids": list(result["ids"]),
    }


def delete_document(
    collection_name: str,
    document_id: int,
):
    """
    Delete a document by its ID.
    """
    client = get_milvus_client()

    client.delete(
        collection_name=collection_name,
        ids=[document_id],
    )

    print(f"Document {document_id} deleted successfully.")


def count_documents(
    collection_name: str,
):
    """
    Return the number of documents in a collection.
    """
    client = get_milvus_client()

    stats = client.get_collection_stats(
        collection_name=collection_name,
    )

    return int(stats["row_count"])


def get_all_documents(
    collection_name: str,
):
    """
    Return all documents in the collection.
    """
    client = get_milvus_client()

    if not client.has_collection(
        collection_name
    ):
        return []

    documents = client.query(
        collection_name=collection_name,
        filter="id >= 0",
        output_fields=[
            "id",
            "text",
        ],
    )

    return documents