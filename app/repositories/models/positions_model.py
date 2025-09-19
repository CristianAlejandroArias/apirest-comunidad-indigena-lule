from sqlalchemy import Column, Integer, String
from app.repositories.database import Base
from sqlalchemy.orm import relationship

class PositionModel(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    
    commissions = relationship("CommissionModel", back_populates="position")
    # Esto crea una relación entre PositionModel y CommissionModel, permitiendo acceder a las comisiones asociadas a una posición
    #back_populates se usa para definir la relación bidireccional entre las dos tablas