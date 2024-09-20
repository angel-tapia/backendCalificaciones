from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from data.generate_pdf import generate_pdf
from models.PdfRequest import PdfRequest
from models.materia import MateriaAlumnos
from models.profesor import Profesor
from data.data_loader import getListaAlumnos420, getListaAlumnos430, getListaAlumnos440, getListaMaterias

main_app = FastAPI()  

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app = APIRouter()

@app.get("/")
async def health_check():
    return "Everything is fine!"

@app.get("/alumnos/{plan}/{subjectId}/{group}", response_model=MateriaAlumnos)
async def getAlumnos(plan: str, subjectId: str, group: str):
    response = None
    if plan == "420":
        response = getListaAlumnos420(subjectId, group)
    elif plan == "430":
        response = getListaAlumnos430(subjectId, group)
    elif plan == "440":
        response = getListaAlumnos440(subjectId, group)
    else:
        raise HTTPException(status_code=404, detail="Plan not found")
    if response is None:
        raise HTTPException(status_code=404, detail="Materia not found")
    return response

@app.get("/materias/{employee_id}", response_model=Profesor)
async def getMaterias(employee_id: str):
    response = getListaMaterias(employee_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return response

@app.post("/pdf", response_class=FileResponse)
async def create_pdf(request: Request, pdf_request: PdfRequest):
    if request.method == "OPTIONS":
        return JSONResponse(status_code=200, content={"body": "OK"})
    
    pdf_file_path = generate_pdf(
        pdf_request.alumno,
        pdf_request.materiaAlumno,
        pdf_request.plan,
        pdf_request.profesor,
        pdf_request.calificacionIncorrecta,
        pdf_request.calificacionCorrecta,
        pdf_request.motivo,
        pdf_request.academia,
        pdf_request.nombreCoordinador,
    )
    
    return FileResponse(pdf_file_path, media_type='application/pdf', filename="output.pdf", status_code=200)

main_app.include_router(app)
