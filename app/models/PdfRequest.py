from pydantic import BaseModel

from app.models.alumno import Alumno
from app.models.materia import MateriaAlumnos
from app.models.profesor import Profesor

class PdfRequest(BaseModel):
    alumno: Alumno
    materiaAlumno: MateriaAlumnos
    profesor: Profesor
    calificacionIncorrecta: str
    calificacionCorrecta: str
    motivo: str