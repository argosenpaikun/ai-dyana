from pydantic import BaseModel

class AddDocumentRequest(BaseModel):
    collection_name: str
    text: str

class DeleteDocumentRequest(BaseModel):
    collection_name: str
    document_id: int