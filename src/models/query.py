from pydantic import BaseModel

class query(BaseModel):
    name: str
    data: str
    