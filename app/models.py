from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    # id: str
    nombre: str
    edad: int
    telefono: str
    fecha_creacion: datetime
