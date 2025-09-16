# Importamos Session para manejar la conexión a la BD
from sqlalchemy.orm import Session

# Importamos el repositorio (acceso directo a la base de datos)
from app.repositories import ParajesRepository
from app.repositories.models.parajes_model import ParajeModel

# Esta clase representa la CAPA DE SERVICIO
# Su función es actuar como intermediaria entre:
# - Los controladores (endpoints de FastAPI)
# - El repositorio (queries SQLAlchemy a la BD)
# Aquí se puede incluir lógica de negocio adicional.
class ParajesService:
    def __init__(self):
        # Creamos una instancia del repositorio de Parajes
        self.repository: ParajesRepository = ParajesRepository()

    # Devuelve todos los parajes llamando al repositorio
    def get_parajes(self, db: Session):
        return self.repository.get_parajes(db)
    
    # Devuelve un solo paraje por ID
    def get_paraje(self, db: Session, paraje_id: int):
        return self.repository.get_paraje(db, paraje_id)
    
    # Crea un nuevo paraje en la BD
    def create_paraje(self, db: Session, paraje: ParajeModel):
        return self.repository.create_paraje(db, paraje)
    
    # Actualiza un paraje existente por su ID
    def update_paraje(self, db: Session, paraje_id: int, paraje: ParajeModel):
        return self.repository.update_paraje(db, paraje_id, paraje)
    
    # Elimina un paraje por su ID
    def delete_paraje(self, db: Session, paraje_id: int):
        return self.repository.delete_paraje(db, paraje_id)
