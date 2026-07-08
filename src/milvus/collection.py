from config import EMBEDDING_DIMENSION
from milvus.client import get_milvus_client

def create_collection(collection_name: str):
    """
    Create a Milvus collection if it does not already exist.
    """
    client = get_milvus_client()
    if client.has_collection(collection_name):
        print(f"Collection '{collection_name}' already exists.")
        return
    client.create_collection(
        collection_name=collection_name,
        dimension=EMBEDDING_DIMENSION,
    )
    print(f"Collection '{collection_name}' created successfully.")

def list_collections():
    """
    List all Milvus collections.
    """
    client = get_milvus_client()
    collections = client.list_collections()
    if not collections:
        print("No collections found.")
        return
    print("Collections:")
    for collection in collections:
        print(f"- {collection}")

def describe_collection(collection_name: str):
    """
    Display information about a collection.
    """
    client = get_milvus_client()
    collection = client.describe_collection(collection_name=collection_name)
    print(f"\nCollection Information: {collection_name}")
    for key, value in collection.items():
        print(f"{key}: {value}")

def drop_collection(collection_name: str):
    """
    Delete a collection from Milvus.
    """
    client = get_milvus_client()
    if not client.has_collection(collection_name):
        print(f"Collection '{collection_name}' does not exist.")
        return
    client.drop_collection(collection_name=collection_name)
    print(f"Collection '{collection_name}' deleted successfully.")