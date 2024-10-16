from pydantic import BaseModel
from typing import List, Dict

from models.alumno import Alumno
from models.materia import MateriaAlumnos
from models.profesor import Profesor

class PdfRequest(BaseModel):
    alumnos: List[Alumno]
    materiaAlumno: MateriaAlumnos
    plan: str
    profesor: Profesor
    calificacionesIncorrectas: Dict[str, str]
    calificacionesCorrectas: Dict[str, str]
    motivo: str
    academia: str
    nombreCoordinador: str
