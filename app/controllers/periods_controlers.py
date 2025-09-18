from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repositories.database import get_db
from app.services import PeriodsService
from app.schemas import Period

router = APIRouter(prefix="/periods", tags=["Periods"])
service = PeriodsService()

@router.get("/period")
def get_periods(db: Session = Depends(get_db)):
    return service.get_periods(db)

@router.get("/period/{period_id}")
def get_period(period_id: int, db: Session = Depends(get_db)):
    return service.get_period(db, period_id)

@router.post("/period")
def create_period(period: Period, db: Session = Depends(get_db)):
    return service.create_period(db, period)

@router.put("/period/{period_id}")
def update_period(period_id: int, period: Period, db: Session = Depends(get_db)):
    return service.update_period(db, period_id, period)

@router.delete("/period/{period_id}")
def delete_period(period_id: int, db: Session = Depends(get_db)):
    return service.delete_period(db, period_id)

