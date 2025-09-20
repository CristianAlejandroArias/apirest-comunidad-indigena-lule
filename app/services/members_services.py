from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import MembersRepository
from app.repositories.models.members_model import MemberModel
from app.repositories.parajes_repository import ParajesRepository

class MembersService:
    def __init__(self):
        self.repository : MembersRepository = MembersRepository()

    def get_members(self, db: Session):
        return self.repository.get_members(db)
    
    def get_member(self,db: Session, member_id: int):
        return self.repository.get_member(db,member_id)
    
    def create_member(self,db: Session, member: MemberModel):
        existing = self.repository.get_member_by_email(db, member.email)
        if existing:
            raise HTTPException(
                status_code=400,
                detail="El email ya está registrado."
            )
        else:
            #Ahora voy a ver que el paraje_id exista
            existing_paraje = ParajesRepository().get_paraje(db, member.paraje_id)
            if not existing_paraje:
                raise HTTPException(
                    status_code=400,
                    detail="El paraje_id no existe."
                ) 
            else:
                return self.repository.create_member(db, member)
    
    def update_member(self, db: Session, member_id: int, member: MemberModel):
        return self.repository.update_member(db,member_id,member)
    
    def delete_member(self, db: Session, member_id: int):
        return self.repository.delete_member(db,member_id)
    