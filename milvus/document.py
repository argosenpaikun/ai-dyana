from milvus.client import get_milvus_client
from milvus.embedding import generate_embedding

def insert_document(
    collection_name: str,
    text: str,
):
    """
    Insert a document into Milvus.
    """
    client = get_milvus_client()
    embedding = generate_embedding(text)
    data = [
        {
            "text": text,
            "embedding": embedding,
        }
    ]
    result = client.insert(
        collection_name=collection_name,
        data=data,
    )
    print("Document inserted successfully.")
    print(result)
    return result

def delete_document(
    collection_name: str,
    document_id: int,
):
    """
    Delete a document.
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