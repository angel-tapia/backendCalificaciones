from typing import Optional
from models.materia import MateriaAlumnos
from utils.Commons import load_json_data

data_plan_420 = load_json_data('data/Listas 420.json')
data_plan_430 = load_json_data('data/Listas 430.json')
data_plan_440 = load_json_data('data/Listas 440.json')

def getAlumnosByKeyAndGroup(data, key: str, group: str) -> Optional[MateriaAlumnos]:
    if len(group) == 2:
        group = '0' + group
    for materia in data:
        if materia['ClaveMateria'] == key and materia['Grupo'] == group:
            return MateriaAlumnos(**materia)
    return None

def getListaAlumnos420(key: str, group: str) -> Optional[MateriaAlumnos]:
    return getAlumnosByKeyAndGroup(data_plan_420, key, group)

def getListaAlumnos430(key: str, group: str) -> Optional[MateriaAlumnos]:
    return getAlumnosByKeyAndGroup(data_plan_430, key, group)

def getListaAlumnos440(key: str, group: str) -> Optional[MateriaAlumnos]:
    return getAlumnosByKeyAndGroup(data_plan_440, key, group)