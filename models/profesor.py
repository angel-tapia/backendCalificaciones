from pydantic import BaseModel
from typing import List
from models.materia import MateriaProfesor

class Profesor(BaseModel):
  EmployeeId: str
  NombreMaestro: str
  Materias: List[MateriaProfesor]
