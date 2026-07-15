from bson import ObjectId
from mongodb.client import get_mongodb

COLLECTION_NAME = "people"

def add_person(
    name: str,
    position: str,
):
    """
    Store a person in MongoDB.
    """
    database = get_mongodb()

    result = database[COLLECTION_NAME].insert_one(
        {
            "name": name,
            "position": position,
            "files": [],
        }
    )

    return str(result.inserted_id)

def get_all_people():
    """
    Return all people.
    """
    database = get_mongodb()

    people = list(
        database[COLLECTION_NAME].find()
    )

    for person in people:
        person["id"] = str(person.pop("_id"))

    return people

def get_person(
    person_id: str,
):
    """
    Return a single person by ID.
    """
    database = get_mongodb()

    person = database[COLLECTION_NAME].find_one(
        {
            "_id": ObjectId(person_id),
        }
    )

    if person is None:
        return None

    person["id"] = str(person.pop("_id"))

    return person

def add_file(
    person_id: str,
    file_id: str,
    filename: str,
    content_type: str,
):
    """
    Add a file reference to a person's profile.
    """
    database = get_mongodb()

    database[COLLECTION_NAME].update_one(
        {
            "_id": ObjectId(person_id),
        },
        {
            "$push": {
                "files": {
                    "file_id": file_id,
                    "filename": filename,
                    "content_type": content_type,
                }
            }
        },
    )