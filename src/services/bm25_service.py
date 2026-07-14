from config import COLLECTION_NAME

from milvus.document import get_all_documents
from bm25.index import (
    build_index,
    get_index
)

def rebuild_index():
    """
    Rebuild the BM25 search index
    """
    documents = get_all_documents(
        COLLECTION_NAME
    )

    build_index(documents)

    print(
        f"BM25 indexed {len(documents)} documents."
    )

def check_health() -> bool:
    """
    Check whether the MB25 index is available
    """
    return get_index() is not None