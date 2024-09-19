from pydantic import BaseModel

class Alumno(BaseModel):
    Matricula: str
    Nombre: str
    Oportunidad: str
    