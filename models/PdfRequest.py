from pydantic import BaseModel

from models.alumno import Alumno
from models.materia import MateriaAlumnos
from models.profesor import Profesor

class PdfRequest(BaseModel):
    alumno: Alumno
    materiaAlumno: MateriaAlumnos
    plan: str
    profesor: Profesor
    calificacionIncorrecta: str
    calificacionCorrecta: str
    motivo: str
    academia: str
    nombreCoordinador: str