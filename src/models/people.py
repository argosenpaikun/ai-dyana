from pydantic import BaseModel

class AddPersonRequest(BaseModel):
    name: str
    position: str