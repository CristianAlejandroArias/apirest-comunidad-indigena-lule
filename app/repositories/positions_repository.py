from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.models.positions_model import PositionModel

class PositionsRepository:
    
    def get_positions(self,db:Session):
        return db.query(PositionModel).all()
    
    def get_position(self, db: Session, position_id: int):
        position = db.query(PositionModel).filter_by(id=position_id).first()
        if not position:
            raise HTTPException(status_code=404, detail="Position not found")
        return position
    
    def create_position(self, db: Session, position: PositionModel):
        new_position = PositionModel(
            name = position.name,
            description = position.description
        )
        db.add(new_position)
        db.commit()
        db.refresh(new_position)
        return new_position
    
    def update_position(self, db: Session, position_id: int, position: PositionModel):
        db_position = db.query(PositionModel).filter_by(id=position_id).first()
        if not db_position:
            raise HTTPException(status_code=404, detail="Position not found")
        if db_position:
            db_position.name = position.name
            db_position.description = position.description
        db.commit()
        db.refresh(db_position)
        return db_position
    
    def delete_position(self, db: Session, position_id: int):
        db_position = db.query(PositionModel).filter(PositionModel.id == position_id).first()
        if db_position:
            db.delete(db_position)
            db.commit()
        return db_position
    
    