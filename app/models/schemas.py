from pydantic import BaseModel

# Request schema
class RequestSchema(BaseModel):
    id: int
    name: str
    description: str

# Response schema
class ResponseSchema(BaseModel):
    success: bool
    message: str
    data: RequestSchema