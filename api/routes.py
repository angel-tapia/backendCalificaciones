from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from data.generate_pdf import generate_pdf
from models.PdfRequest import PdfRequest
from models.materia import MateriaAlumnos
from models.profesor import Profesor
from data.data_loader import getListaAlumnos420, getListaAlumnos430, getListaAlumnos440, getListaMaterias

router = APIRouter()

@router.get("/")
async def health_check():
    return "Everything is fine!"