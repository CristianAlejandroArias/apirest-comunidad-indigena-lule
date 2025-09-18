from sqlalchemy import Column, Integer, String, Date, func 
from app.repositories.database import Base
from sqlalchemy.orm import relationship

class PeriodModel(Base):
    __tablename__="periods"

    id = Column(Integer, primary_key= True, index=True)
    start_period = Column(Date, index=True)
    end_period = Column(Date, index=True)

