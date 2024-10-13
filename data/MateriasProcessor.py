from typing import Optional
from models.profesor import Profesor
from utils.Commons import load_json_data

materias_profesores = load_json_data('data/professors_subjects.json')

def getListaMaterias(employee_id: str) -> Optional[Profesor]:
    for profesor in materias_profesores:
        if profesor['EmployeeId'] == employee_id:
            return profesor
    return None