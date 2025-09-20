from sqlalchemy.orm import Session
from app.repositories import CommissionsRepository
from app.repositories.models.commissions_model import CommissionModel
from app.repositories import MembersRepository, PositionsRepository, PeriodsRepository 
# Importo los repositorios necesarios para validar las claves foráneas

class CommissionsService:
    def __init__(self):
        self.repository : CommissionsRepository = CommissionsRepository()

    def get_commissions(self, db: Session):
        return self.repository.get_commissions(db)
    
    def get_commission(self,db: Session, commission_id: int):
        return self.repository.get_commission(db,commission_id)
    
    def create_commission(self,db: Session, commission: CommissionModel):
        #Voy a chequear que exita el commission.member_id, position_id y period_id
        exiting_member = MembersRepository().get_member(db, commission.member_id)
        #que pasa si no existe? Levanto una excepción en el repositorio
        #si existe, sigo
        exiting_position = PositionsRepository().get_position(db, commission.position_id)
        exiting_period = PeriodsRepository().get_period(db, commission.period_id)
        return self.repository.create_commission(db, commission)
    
    def update_commission(self, db: Session, commission_id: int, commission: CommissionModel):
        return self.repository.update_commission(db,commission_id,commission)
    
    def delete_commission(self, db: Session, commission_id: int):
        return self.repository.delete_commission(db,commission_id)
    
    
