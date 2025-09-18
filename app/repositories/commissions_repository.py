from fastapi import HttpException
from sqlalchemy.orm import Session
from app.repositories.models.commissions_model import CommissionModel

class CommissionsRepository:
    
    def get_commissions(self,db:Session):
        return db.query(CommissionModel).all()
    
    def get_commission(self, db: Session, commission_id: int):
        commission = db.query(CommissionModel).filter_by(id=commission_id).first()
        if not commission:
            raise HttpException(status_code=404, detail="Commission not found")
        return commission
    
    def create_commission(self, db: Session, commission: CommissionModel):
        new_commission = CommissionModel(
            member_id = commission.member_id,
            position_id = commission.position_id,
            period_id = commission.period_id
        )
        db.add(new_commission)
        db.commit()
        db.refresh(new_commission)
        return new_commission
    
    def update_commission(self, db: Session, commission_id: int, commission: CommissionModel):
        db_commission = db.query(CommissionModel).filter_by(id=commission_id).first()
        if not db_commission:
            raise HttpException(status_code=404, detail="Commission not found")
        if db_commission:
            db_commission.member_id = commission.member_id
            db_commission.position_id = commission.position_id
            db_commission.period_id = commission.period_id
        db.commit()
        db.refresh(db_commission)
        return db_commission
    
    def delete_commission(self, db: Session, commission_id: int):
        db_commission = db.query(CommissionModel).filter(CommissionModel.id == commission_id).first()
        if db_commission:
            db.delete(db_commission)
            db.commit()
        return db_commission