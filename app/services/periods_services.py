from sqlalchemy.orm import Session
from app.repositories import PeriodsRepository
from app.repositories.models.periods_model import PeriodModel

class PeriodsService:
    def __init__(self):
        self.repository : PeriodsRepository = PeriodsRepository()

    def get_periods(self, db: Session):
        return self.repository.get_periods(db)
    
    def get_period(self,db: Session, period_id: int):
        return self.repository.get_period(db,period_id)
    
    def create_period(self,db: Session, period: PeriodModel):
        return self.repository.create_period(db, period)
    
    def update_period(self, db: Session, period_id: int, period: PeriodModel):
        return self.repository.update_period(db,period_id,period)
    
    def delete_period(self, db: Session, period_id: int):
        return self.repository.delete_period(db,period_id)
    
