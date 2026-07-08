from pymilvus import MilvusClient
from config import MILVUS_URI

def get_milvus_client():
    """
    Create and return a Milvus client.
    """
    client = MilvusClient(
        uri=MILVUS_URI,
    )
    return client