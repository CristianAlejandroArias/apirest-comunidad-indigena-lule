from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repositories.database import get_db
from app.services import MembersService
from app.schemas import Member

router = APIRouter(prefix="/members", tags=["Members"])
service = MembersService()

@router.get("/member")
def get_members(db: Session = Depends(get_db)):
    return service.get_members(db)

@router.get("/member/{member_id}")
def get_member(member_id: int, db: Session = Depends(get_db)):
    return service.get_member(db, member_id)

@router.post("/member")
def create_member(member: Member, db: Session = Depends(get_db)):
    return service.create_member(db, member)

@router.put("/member/{member_id}")
def update_member(member_id: int, member: Member, db: Session = Depends(get_db)):
    return service.update_member(db, member_id, member)

@router.delete("/member/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    return service.delete_member(db, member_id)


