from milvus.client import get_milvus_client
from milvus.embedding import generate_embedding

def search_documents(
    collection_name: str,
    query: str,
    limit: int = 5,
):
    """
    Search for similar documents in Milvus.
    """
    client = get_milvus_client()
    query_embedding = generate_embedding(query)
    results = client.search(
        collection_name=collection_name,
        data=[query_embedding],
        limit=limit,
        output_fields=["text"],
    )
    documents = []
    for result in results[0]:
        documents.append(
            {
                "id": result["id"],
                "score": result["distance"],
                "text": result["entity"]["text"],
            }
        )
    return documents