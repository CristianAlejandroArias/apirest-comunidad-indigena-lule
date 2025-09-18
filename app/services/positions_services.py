from sqlalchemy.orm import Session
from app.repositories import PositionsRepository
from app.repositories.models.positions_model import PositionModel

class PositionsService:
    def __init__(self):
        self.repository : PositionsRepository = PositionsRepository()

    def get_positions(self, db: Session):
        return self.repository.get_positions(db)
    
    def get_position(self,db: Session, position_id: int):
        return self.repository.get_position(db,position_id)
    
    def create_position(self,db: Session, position: PositionModel):
        return self.repository.create_position(db, position)
    
    def update_position(self, db: Session, position_id: int, position: PositionModel):
        return self.repository.update_position(db,position_id,position)
    
    def delete_position(self, db: Session, position_id: int):
        return self.repository.delete_position(db,position_id)
    