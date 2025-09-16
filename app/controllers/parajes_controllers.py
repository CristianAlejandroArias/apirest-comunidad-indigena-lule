# Importamos APIRouter para definir rutas (endpoints)
# Importamos Depends para inyectar dependencias (como la BD)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# get_db nos da una sesión de base de datos
from app.repositories.database import get_db
# Importamos el servicio que maneja la lógica de negocio
from app.services import ParajesService
# Importamos el esquema Pydantic para validar la entrada/salida
from app.schemas import Paraje

# Creamos un router con prefijo "/parajes" y etiqueta "Parajes"
router = APIRouter(prefix="/parajes", tags=["Parajes"])
# Instanciamos el servicio de Parajes
service = ParajesService()

# ENDPOINT GET: devuelve todos los parajes
@router.get("/paraje")
def get_parajes(db: Session = Depends(get_db)):
    # Llama al servicio que a su vez llama al repositorio
    return service.get_parajes(db)

# ENDPOINT GET: devuelve un solo paraje por ID
@router.get("/paraje/{paraje_id}")
def get_paraje(paraje_id: int, db: Session = Depends(get_db),):
    return service.get_paraje(db, paraje_id)

# ENDPOINT POST: crea un nuevo paraje
@router.post("/paraje")
def create_paraje(paraje: Paraje, db: Session = Depends(get_db)):
    # "Paraje" es un esquema Pydantic que valida la entrada (JSON)
    return service.create_paraje(db, paraje)

# ENDPOINT PUT: actualiza un paraje existente por ID
@router.put("/paraje/{paraje_id}")
def update_paraje(paraje_id: int, paraje: Paraje, db: Session = Depends(get_db)):
    return service.update_paraje(db, paraje_id, paraje)

# ENDPOINT DELETE: elimina un paraje por ID
@router.delete("/paraje/{paraje_id}")
def delete_paraje(paraje_id:int, db: Session = Depends(get_db)):
    return service.delete_paraje(db, paraje_id)
