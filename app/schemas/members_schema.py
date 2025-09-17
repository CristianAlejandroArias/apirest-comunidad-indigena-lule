from pydantic import BaseModel
from datetime import date
from typing import Optional

class Member(BaseModel):
    dni: int
    name: str
    last_name: str
    address: str
    phone: str
    email: str
    birth_date: date 
    join_date: Optional[date] = None
    paraje_id: int









