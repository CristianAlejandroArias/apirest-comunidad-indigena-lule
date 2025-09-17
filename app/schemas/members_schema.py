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
    paraje_id: int
    join_date: Optional[date] = None
    # join_date es opcional porque se asigna automaticamente con default=func.current_date al crear el miembro









