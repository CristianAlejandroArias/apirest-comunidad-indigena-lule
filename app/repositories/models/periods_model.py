from sqlalchemy import Column, Integer, String, Date, func 
from app.repositories.database import Base
from sqlalchemy.orm import relationship

class PeriodModel(Base):
    __tablename__="periods"

    id = Column(Integer, primary_key= True, index=True)
    start_period = Column(Date, index=True)
    end_period = Column(Date, index=True)

    commissions = relationship("CommissionModel", back_populates="period")
    # Esto crea una relación entre PeriodModel y CommissionModel, permitiendo acceder a las comisiones asociadas a un período
    #back_populates se usa para definir la relación bidireccional entre las dos tablas

    