from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repositories.database import get_db
from app.services import PositionsService
from app.schemas import Position

router = APIRouter(prefix="/positions", tags=["Positions"])
service = PositionsService()

@router.get("/position")
def get_positions(db: Session = Depends(get_db)):
    return service.get_positions(db)

@router.get("/position/{position_id}")
def get_position(position_id: int, db: Session = Depends(get_db)):
    return service.get_position(db, position_id)

@router.post("/position")
def create_position(position: Position, db: Session = Depends(get_db)):
    return service.create_position(db, position)

@router.put("/position/{position_id}")
def update_position(position_id: int, position: Position, db: Session = Depends(get_db)):
    return service.update_position(db, position_id, position)

@router.delete("/position/{position_id}")
def delete_position(position_id: int, db: Session = Depends(get_db)):
    return service.delete_position(db, position_id)



