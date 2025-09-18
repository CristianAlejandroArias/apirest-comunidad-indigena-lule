from sqlalchemy import Column, Integer, ForeignKey
from app.repositories.database import Base
from sqlalchemy.orm import relationship

class CommissionModel(Base):
    __tablename__ = "commissions"

    id = Column(Integer, primary_key=True, index=True)

    member_id = Column(Integer, ForeignKey("members.id"))
    member = relationship("MemberModel", back_populates="commissions")
    # Esto crea una relación entre CommissionModel y MemberModel, permitiendo acceder al miembro asociado a una comisión
    #back_populates se usa para definir la relación bidireccional entre las dos tablas
    position_id = Column(Integer, ForeignKey("positions.id"))
    position = relationship("PositionModel", back_populates="commissions")
    # Esto crea una relación entre CommissionModel y PositionModel, permitiendo acceder a la posición asociada a una comisión
    #back_populates se usa para definir la relación bidireccional entre las dos tablas
    period_id = Column(Integer, ForeignKey("periods.id"))
    period = relationship("PeriodModel", back_populates="commissions")
    # Esto crea una relación entre CommissionModel y PeriodModel, permitiendo acceder al período asociado a una comisión
    #back_populates se usa para definir la relación bidireccional entre las dos tablas  

