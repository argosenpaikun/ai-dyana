from bson import ObjectId
from mongodb.client import get_gridfs

def upload_file(
    filename: str,
    content_type: str,
    data: bytes,
):
    """
    Store a file in GridFS.
    """
    gridfs = get_gridfs()

    file_id = gridfs.put(
        data,
        filename=filename,
        content_type=content_type,
    )

    return str(file_id)

def download_file(
    file_id: str,
):
    """
    Retrieve a file from GridFS.
    """
    gridfs = get_gridfs()

    return gridfs.get(
        ObjectId(file_id)
    )

def delete_file(
    file_id: str,
):
    """
    Delete a file from GridFS.
    """
    gridfs = get_gridfs()

    gridfs.delete(
        ObjectId(file_id)
    )