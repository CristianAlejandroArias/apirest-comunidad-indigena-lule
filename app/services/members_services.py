from sqlalchemy.orm import Session
from app.repositories import MembersRepository
from app.repositories.models.members_model import MemberModel

class MembersService:
    def __init__(self):
        self.repository : MembersRepository = MembersRepository()

    def get_members(self, db: Session):
        return self.repository.get_members(db)
    
    def get_member(self,db: Session, member_id: int):
        return self.repository.get_member(db,member_id)
    
    def create_member(self,db: Session, member: MemberModel):
        return self.repository.create_member(db, member)
    
    def update_member(self, db: Session, member_id: int, member: MemberModel):
        return self.repository.update_member(db,member_id,member)
    
    def delete_member(self, db: Session, member_id: int):
        return self.repository.delete_member(db,member_id)