from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.models.members_model import MemberModel

class MembersRepository:
    
    def get_members(self,db:Session):
        return db.query(MemberModel).all()
    
    def get_member(self, db: Session, member_id: int):
        member = db.query(MemberModel).filter_by(id=member_id).first()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        return member
    
    def create_member(self, db: Session, member: MemberModel):
        new_member = MemberModel(
            dni = member.dni,
            name = member.name,
            last_name = member.last_name,
            adreess = member.address,
            phone = member.phone,
            email = member.email,
            birth_date = member.birth_date,
            paraje_id = member.paraje_id
            #join_date = member.join_date (esto se asigna automaticamente con default=func.current_date
        )
        db.add(new_member)
        db.commit()
        db.refresh(new_member)
        return new_member
    
    def update_member(self, db: Session, member_id: int, member: MemberModel):
        db_member = db.query(MemberModel).filter_by(id=member_id).first()
        if not db_member:
            raise HTTPException(status_code=404, detail="Member not found")
        if db_member:
            db_member.dni = member.dni
            db_member.name = member.name
            db_member.last_name = member.last_name
            db_member.address = member.address
            db_member.phone = member.phone
            db_member.email = member.email
            db_member.birth_date = member.birth_date
            db_member.paraje_id = member.paraje_id
            #join_date no se actualiza porque se asigna automaticamente con default=func.current_date al crear el miembro
        db.commit()
        db.refresh(db_member)
        return db_member
    
    def delete_member(self, db: Session, member_id: int):
        db_member = db.query(MemberModel).filter(MemberModel.id == member_id).first()
        if db_member:
            db.delete(db_member)
            db.commit()
        return db_member
    
    