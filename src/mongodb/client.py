from pymongo import MongoClient
from gridfs import GridFS

from config import (
    MONGODB_URI,
    MONGODB_DATABASE,
)
_client = MongoClient(MONGODB_URI)
_database = _client[MONGODB_DATABASE]

_gridfs = GridFS(_database)

def get_mongodb():
    """
    Return the MongoDB database instance.
    """
    return _database

def get_gridfs():
    """
    Return the GridFS instance.
    """
    return _gridfs

def check_health() -> bool:
    """
    Check MongoDB connectivity.
    """
    try:
        _client.admin.command("ping")
        return True
    except Exception:
        return False