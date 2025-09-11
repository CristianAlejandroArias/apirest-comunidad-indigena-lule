from sqlalchemy.orm import Session

from app.repositories import ParajesRepository
from app.repositories.models.parajes_model import ParajeModel

class ParajesService:
    def __init__(self):
        self.repository : ParajesRepository = ParajesRepository()

    def get_parajes(self, db: Session):
        return self.repository.get_parajes(db)
    
    def get_paraje(self,db: Session, paraje_id: int):
        return self.repository.get_paraje(db,paraje_id)
    
    def create_paraje(self,db: Session, paraje: ParajeModel):
        return self.repository.create_paraje(db, paraje)
    
    def update_paraje(self, db: Session, paraje_id: int, paraje: ParajeModel):
        return self.repository.update_paraje(db,paraje_id,paraje)
    
    def delete_paraje(self, db: Session, paraje_id: int):
        return self.repository.delete_paraje(db,paraje_id)
