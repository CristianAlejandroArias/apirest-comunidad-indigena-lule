from sqlalchemy import Column, Integer, String
from app.repositories.database import Base

class PositionModel(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    