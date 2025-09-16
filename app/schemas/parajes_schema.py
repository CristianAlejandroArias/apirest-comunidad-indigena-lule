# Importamos BaseModel de Pydantic
# Pydantic sirve para validar y serializar datos en FastAPI
from pydantic import BaseModel


# Definimos un esquema (schema) llamado Paraje
# Los esquemas NO son tablas, son modelos de validación de datos
class Paraje(BaseModel):
    # Campo "name", que debe ser de tipo string
    # Cuando alguien envíe datos a la API, FastAPI validará que "name" sea texto
    name: str
