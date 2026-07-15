from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
)

from models.people import AddPersonRequest

from mongodb.people import (
    add_person,
    get_all_people,
    get_person,
    add_file,
)

from mongodb.files import upload_file

router = APIRouter(
    prefix="/people",
    tags=["People"],
)

@router.post("/")
def create_person(
    request: AddPersonRequest,
):
    person_id = add_person(
        name=request.name,
        position=request.position,
    )

    return {
        "status": "success",
        "message": f"Person '{request.name}' added successfully.",
        "person": {
            "id": person_id,
            "name": request.name,
            "position": request.position,
        },
    }

@router.get("/")
def list_people():
    people = get_all_people()

    return {
        "status": "success",
        "count": len(people),
        "people": people,
    }

@router.get("/{person_id}")
def get_person_details(
    person_id: str,
):
    person = get_person(person_id)

    if person is None:
        raise HTTPException(
            status_code=404,
            detail="Person not found.",
        )

    return {
        "status": "success",
        "person": person,
    }

@router.post("/{person_id}/files")
def upload_file_endpoint(
    person_id: str,
    file: UploadFile = File(...),
):
    contents = file.file.read()

    file_id = upload_file(
        filename=file.filename,
        content_type=file.content_type,
        data=contents,
    )

    add_file(
        person_id=person_id,
        file_id=file_id,
        filename=file.filename,
        content_type=file.content_type,
    )

    return {
        "status": "success",
        "message": "File uploaded successfully.",
        "file": {
            "file_id": file_id,
            "filename": file.filename,
            "content_type": file.content_type,
        },
    }