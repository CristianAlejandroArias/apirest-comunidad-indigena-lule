from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.repositories.database import get_db
from app.services import CommissionsService
from app.schemas import Commission

router = APIRouter(prefix="/commissions", tags=["Commissions"])
service = CommissionsService()

@router.get("/commission")
def get_commissions(db: Session = Depends(get_db)):
    return service.get_commissions(db)

@router.get("/commission/{commission_id}")
def get_commission(commission_id: int, db: Session = Depends(get_db)):
    return service.get_commission(db, commission_id)

@router.post("/commission")
def create_commission(commission: Commission, db: Session = Depends(get_db)):
    return service.create_commission(db, commission)

@router.put("/commission/{commission_id}")
def update_commission(commission_id: int, commission: Commission, db: Session = Depends(get_db)):
    return service.update_commission(db, commission_id, commission)

@router.delete("/commission/{commission_id}")
def delete_commission(commission_id: int, db: Session = Depends(get_db)):
    return service.delete_commission(db, commission_id)

