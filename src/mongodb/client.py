from pymongo import MongoClient

from config import (
    MONGODB_URI,
    MONGODB_DATABASE,
)

_client = MongoClient(MONGODB_URI)
_database = _client[MONGODB_DATABASE]

def get_mongodb():
    """
    Return the MongoDB database instance.
    """
    return _database

def check_health() -> bool:
    """
    Check MongoDB connectivity
    """
    try:
        _client.admin.command("ping")
        return True
    except:
        return False