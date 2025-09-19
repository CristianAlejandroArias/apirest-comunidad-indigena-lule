from sqlalchemy import Column, Integer, String, Date, ForeignKey , func
from app.repositories.database import Base
from sqlalchemy.orm import relationship


class MemberModel(Base):
    __tablename__= "members"

    id = Column (Integer, primary_key=True, index=True)
    dni = Column(Integer, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    address = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, index=True)
    birth_date = Column(Date, index=True)
    join_date = Column(Date, default=func.current_date, index=True)
    
    paraje_id = Column(Integer, ForeignKey("parajes.id"))
    paraje = relationship("ParajeModel", back_populates="members")
    # Esto crea una relación entre MemberModel y ParajeModel, permitiendo acceder al paraje asociado a un miembro
    #back_populates se usa para definir la relación bidireccional entre las dos tablas

    commissions = relationship("CommissionModel", back_populates="member")
    # Esto crea una relación entre MemberModel y CommissionModel, permitiendo acceder a las com isiones asociadas a un miembro
    #back_populates se usa para definir la relación bidireccional entre las dos tablas        