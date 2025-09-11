from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.models.parajes_model import ParajeModel

class ParajesRepository:
    
    def get_parajes(self,db:Session):
        return db.query(ParajeModel).all()
    
    def get_paraje(self, db: Session, paraje_id: int):
        paraje = db.query(ParajeModel).filter_by(id=paraje_id).first()
        if not paraje:
            raise HTTPException(status_code=404, detail="Paraje not found")
        return paraje
    
    def create_paraje(self, db: Session, paraje: ParajeModel):
        new_paraje = ParajeModel(
            name = paraje.name
        )
        db.add(new_paraje)
        db.commit()
        db.refresh(new_paraje)
        return new_paraje
    
    def update_paraje(self, db: Session, paraje_id: int, paraje: ParajeModel):
        db_paraje = db.query(ParajeModel).filter_by(id=paraje_id).first()
        if not db_paraje:
            raise HTTPException(status_code=404, detail="Paraje not found")
        if db_paraje:
            db_paraje.name = paraje.name
        db.commit()
        db.refresh(db_paraje)
        return db_paraje
    
    def delete_paraje(self, db: Session, paraje_id: int):
        db_paraje = db.query(ParajeModel).filter(ParajeModel.id == paraje_id).first()
        if db_paraje:
            db.delete(db_paraje)
            db.commit()
        return db_paraje
    