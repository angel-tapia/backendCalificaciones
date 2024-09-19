from pydantic import BaseModel
from models.alumno import Alumno
from typing import List

class MateriaProfesor(BaseModel):
  ClaveMateria: str
  NombreMateria: str
  Grupo: str
  Plan: str
  Academia: str

class MateriaAlumnos(BaseModel):
  ClaveMateria: str
  NombreMateria: str
  Grupo: str
  Alumnos: List[Alumno]
