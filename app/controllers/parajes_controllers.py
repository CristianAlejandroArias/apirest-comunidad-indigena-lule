from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services import ParajesService
from app.schemas import Paraje

router = APIRouter(prefix="/parajes", tags=["Parajes"])
service = ParajesService()

@router.get("/paraje")
def get_parajes(db: Session = Depends(get_db)):
    return service.get_parajes(db)

@router.get("/paraje/{paraje_id}")
def get_paraje(paraje_id: int, db: Session = Depends(get_db),):
    return service.get_paraje(db,paraje_id)

@router.post("/paraje")
def create_paraje(paraje: Paraje, db: Session = Depends(get_db)):
    return service.create_paraje(db,paraje)

@router.put("/paraje/{paraje_id}")
def update_paraje(paraje_id: int, paraje: Paraje, db: Session = Depends(get_db)):
    return service.update_paraje(db,paraje_id, paraje)

@router.delete("/paraje/{paraje_id}")
def delete_paraje(paraje_id:int, db: Session = Depends(get_db)):
    return service.delete_paraje(db,paraje_id)

