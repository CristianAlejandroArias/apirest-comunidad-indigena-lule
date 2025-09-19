from sqlalchemy.orm import Session
from app.repositories import CommissionsRepository
from app.repositories.models.commissions_model import CommissionModel

class CommissionsService:
    def __init__(self):
        self.repository : CommissionsRepository = CommissionsRepository()

    def get_commissions(self, db: Session):
        return self.repository.get_commissions(db)
    
    def get_commission(self,db: Session, commission_id: int):
        return self.repository.get_commission(db,commission_id)
    
    def create_commission(self,db: Session, commission: CommissionModel):
        return self.repository.create_commission(db, commission)
    
    def update_commission(self, db: Session, commission_id: int, commission: CommissionModel):
        return self.repository.update_commission(db,commission_id,commission)
    
    def delete_commission(self, db: Session, commission_id: int):
        return self.repository.delete_commission(db,commission_id)
    
    
