from pydantic import BaseModel

class current_user(BaseModel):
    name: str
    