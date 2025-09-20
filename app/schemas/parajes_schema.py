from pydantic import BaseModel

class Paraje(BaseModel):
    name: str
    
    class Config:
        orm_mode = True