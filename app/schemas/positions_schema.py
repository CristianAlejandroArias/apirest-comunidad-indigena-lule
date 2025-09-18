from pydantic import BaseModel

class Position(BaseModel):
    name: str
    description: str
    