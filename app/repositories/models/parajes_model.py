# Importamos lo necesario de SQLAlchemy
from sqlalchemy import Column, Integer, String        # Columnas y tipos de datos
from app.repositories.database import Base            # Nuestra clase Base para modelos (creada en database.py)
from sqlalchemy.orm import relationship

# Definimos un modelo llamado "ParajeModel"
class ParajeModel(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "parajes"

    # Columnas de la tabla:
    id = Column(Integer, primary_key=True, index=True)
    # - Integer → tipo de dato entero
    # - primary_key=True → clave primaria de la tabla
    # - index=True → crea un índice para búsquedas rápidas por "id"

    name = Column(String, index=True)
    # - String → tipo de dato texto
    # - index=True → también se puede buscar más rápido por "name"

    members = relationship("MemberModel", back_populates="paraje")

    