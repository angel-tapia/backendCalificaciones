import json
from typing import Optional
from models.materia import MateriaAlumnos
from models.profesor import Profesor

def load_json_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

data_plan_420 = load_json_data('data/Listas 420.json')
data_plan_430 = load_json_data('data/Listas 430.json')
data_plan_440 = load_json_data('data/Listas 440.json')
materias_profesores = load_json_data('data/professors_subjects.json')

def getListaMaterias(employee_id: str) -> Optional[Profesor]:
    for profesor in materias_profesores:
        if profesor['EmployeeId'] == employee_id:
            return profesor
    return None

def get_materia_by_key_and_group(data, key: str, group: str) -> Optional[MateriaAlumnos]:
    if len(group) == 2:
        group = '0' + group
    for materia in data:
        if materia['ClaveMateria'] == key and materia['Grupo'] == group:
            return MateriaAlumnos(**materia)
    return None

def getListaAlumnos420(key: str, group: str) -> Optional[MateriaAlumnos]:
    return get_materia_by_key_and_group(data_plan_420, key, group)

def getListaAlumnos430(key: str, group: str) -> Optional[MateriaAlumnos]:
    return get_materia_by_key_and_group(data_plan_430, key, group)

def getListaAlumnos440(key: str, group: str) -> Optional[MateriaAlumnos]:
    return get_materia_by_key_and_group(data_plan_440, key, group)
