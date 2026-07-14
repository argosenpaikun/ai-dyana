from pydantic import BaseModel

class AddDocumentRequest(BaseModel):
    collection_name: str
    text: str