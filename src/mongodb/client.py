from pymongo import MongoClient

from config import (
    MONGODB_URI,
    MONGODB_DATABASE
)

def get_mongodb():
    client = MongoClient(
        MONGODB_URI
    )

    return client[MONGODB_DATABASE]