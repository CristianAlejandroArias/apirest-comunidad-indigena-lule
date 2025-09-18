from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.models.periods_model import PeriodModel

class PeriodsRepository:
    
    def get_periods(self,db:Session):
        return db.query(PeriodModel).all()
    
    def get_period(self, db: Session, period_id: int):
        period = db.query(PeriodModel).filter_by(id=period_id).first()
        if not period:
            raise HTTPException(status_code=404, detail="Period not found")
        return period
    
    def create_period(self, db: Session, period: PeriodModel):
        new_period = PeriodModel(
            start_period = period.start_period,
            end_period = period.end_period
        )
        db.add(new_period)
        db.commit()
        db.refresh(new_period)
        return new_period
    
    def update_period(self, db: Session, period_id: int, period: PeriodModel):
        db_period = db.query(PeriodModel).filter_by(id=period_id).first()
        if not db_period:
            raise HTTPException(status_code=404, detail="Period not found")
        if db_period:
            db_period.start_period = period.start_period
            db_period.end_period = period.end_period
        db.commit()
        db.refresh(db_period)
        return db_period
    
    def delete_period(self, db: Session, period_id: int):
        db_period = db.query(PeriodModel).filter(PeriodModel.id == period_id).first()
        if db_period:
            db.delete(db_period)
            db.commit()
        return db_period