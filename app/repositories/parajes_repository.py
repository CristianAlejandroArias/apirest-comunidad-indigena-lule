# Importamos HTTPException para manejar errores de API en FastAPI
from fastapi import HTTPException
# Importamos Session de SQLAlchemy para manejar la conexión con la BD
from sqlalchemy.orm import Session

# Importamos el modelo de la tabla "parajes"
from app.repositories.models.parajes_model import ParajeModel


# Repositorio = capa que interactúa directamente con la base de datos
class ParajesRepository:
    
    # Obtiene todos los registros de la tabla "parajes"
    def get_parajes(self, db: Session):
        return db.query(ParajeModel).all()
    
    # Obtiene un solo registro de "parajes" según su id
    def get_paraje(self, db: Session, paraje_id: int):
        paraje = db.query(ParajeModel).filter_by(id=paraje_id).first()
        if not paraje:
            # Si no existe, lanzamos error HTTP 404 (no encontrado)
            raise HTTPException(status_code=404, detail="Paraje not found")
        return paraje
    
    # Crea un nuevo registro en la tabla "parajes"
    def create_paraje(self, db: Session, paraje: ParajeModel):
        new_paraje = ParajeModel(
            name = paraje.name  # asignamos el nombre
        )
        db.add(new_paraje)     # lo agregamos a la sesión
        db.commit()            # confirmamos los cambios en la BD
        db.refresh(new_paraje) # actualizamos el objeto con el ID generado
        return new_paraje
    
    # Actualiza un registro existente según su id
    def update_paraje(self, db: Session, paraje_id: int, paraje: ParajeModel):
        db_paraje = db.query(ParajeModel).filter_by(id=paraje_id).first()
        if not db_paraje:
            raise HTTPException(status_code=404, detail="Paraje not found")
        if db_paraje:
            db_paraje.name = paraje.name  # modificamos el campo "name"
        db.commit()
        db.refresh(db_paraje)
        return db_paraje
    
    # Elimina un registro según su id
    def delete_paraje(self, db: Session, paraje_id: int):
        db_paraje = db.query(ParajeModel).filter(ParajeModel.id == paraje_id).first()
        if db_paraje:
            db.delete(db_paraje)  # borramos el registro
            db.commit()           # confirmamos el cambio
        return db_paraje
