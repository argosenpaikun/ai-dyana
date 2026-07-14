from pymilvus import MilvusClient
from config import MILVUS_URI

_client = MilvusClient(
    uri=MILVUS_URI
)

def get_milvus_client():
    """
    Return the Milvus client
    """
    return _client

def check_health() -> bool:
    """
    Check Milvus connectivity
    """
    try:
        _client.list_collections()
        return True
    except:
        return False