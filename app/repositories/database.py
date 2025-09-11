# Importamos lo necesario de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definimos la URL de conexión a la base de datos (en este caso SQLite, archivo local)
DATABASE_URL = "sqlite:///.comunidadLule.db"

# Creamos el motor de conexión a la base de datos
# "check_same_thread=False" es necesario en SQLite cuando usamos la DB en entornos con varios hilos (ejemplo: FastAPI)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Creamos una clase fábrica de sesiones para interactuar con la DB
# - autocommit: si se pone en True, confirma los cambios automáticamente (mejor mantener en False)
# - autoflush: si se pone en True, envía los cambios automáticamente a la DB antes de cada query
# - bind: indica con qué motor de base de datos se asocia
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base: clase base de la que heredarán los modelos (tablas) de SQLAlchemy
Base = declarative_base()

# Dependencia para obtener una sesión de DB en cada request (ejemplo: en FastAPI)
def get_db():
    db = SessionLocal()  # Creamos una sesión
    try:
        yield db          # La retornamos para usarla en la consulta
    finally:
        db.close()        # Al terminar, cerramos la conexión para liberar recursos
