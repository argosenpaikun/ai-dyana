from pymilvus import MilvusClient, DataType
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
    
    schema = MilvusClient.create_schema(
        auto_id=True,
        enable_dynamic_false=False
    )

    schema.add_field(
        field_name="id", 
        datatype=DataType.INT64,
        is_primary=True
    )

    schema.add_field(
        field_name="text",
        datatype=DataType.VARCHAR,
        max_length=65535
    )

    schema.add_field(
        field_name="vector",
        datatype=DataType.FLOAT_VECTOR,
        dim=EMBEDDING_DIMENSION
    )

    index_params = client.prepare_index_params()

    index_params.add_index(
        field_name="vector",
        index_type="AUTOINDEX",
        metric_type="COSINE"
    )

    client.create_collection(
        collection_name=collection_name,
        schema=schema,
        index_params=index_params,
    )

    client.load_collection(
        collection_name=collection_name
    )

    print(f"Collection '{collection_name}' created successfully.")

def list_collections():
    """
    List all Milvus collections.
    """
    client = get_milvus_client()
    collections = client.list_collections()
    
    return collections

def describe_collection(collection_name: str):
    """
    Display information about a collection.
    """
    client = get_milvus_client()
    return client.describe_collection(collection_name=collection_name)

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