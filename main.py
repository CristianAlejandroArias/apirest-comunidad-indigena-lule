# Importamos FastAPI para crear la aplicación principal
from fastapi import FastAPI
# Importamos los routers de controladores de "parajes" y "miembros"
from app.controllers import parajes_router
#from app.controllers import miembros_router
# Importamos Base y engine para inicializar las tablas en la base de datos
from app.repositories.database import Base, engine

# Creamos la instancia principal de la aplicación FastAPI
app = FastAPI()

# Esto crea automáticamente todas las tablas definidas en los modelos SQLAlchemy
# (ejecuta CREATE TABLE si no existen en la base de datos)
Base.metadata.create_all(bind=engine)

# Registramos el router de "parajes" con prefijo "/api/v1"
app.include_router(router=parajes_router, prefix=f"/api/v1")

# ⚠️ Nota: también deberías incluir el router de "miembros"
# porque lo importaste pero no lo estás registrando todavía:
# app.include_router(router=miembros_router, prefix=f"/api/v1")
