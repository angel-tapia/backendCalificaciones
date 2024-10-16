from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import FileResponse
from data.generate_pdf import generate_pdf
from models.materia import MateriaAlumnos
from models.profesor import Profesor
from models.pdfRequest import PdfRequest
from data.ListasProcessor import getListaAlumnos420, getListaAlumnos430, getListaAlumnos440
from data.MateriasProcessor import getListaMaterias
from data.EmployeesProcessor import getEmployeeIdByEmail
from utils.TokenVerifier import verify_token

app = APIRouter()

def verify_auth_token(request: Request):
    token = request.headers.get('Authorization')

    if token is None:
        raise HTTPException(status_code=401, detail="Token not found")
    
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Token is invalid or expired.")
    
    return True

@app.get("/api/alumnos/{plan}/{subjectId}/{group}", response_model=MateriaAlumnos, dependencies=[Depends(verify_auth_token)])
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

@app.get("/api/materias/{employee_id}", response_model=Profesor, dependencies=[Depends(verify_auth_token)])
async def getMaterias(employee_id: str):
    response = getListaMaterias(employee_id)

    if response is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return response

@app.post("/api/pdf", response_class=FileResponse, dependencies=[Depends(verify_auth_token)])
async def create_pdf(pdf_request: PdfRequest):
    pdf_file_path = generate_pdf(
        pdf_request.alumnos,
        pdf_request.materiaAlumno,
        pdf_request.plan,
        pdf_request.profesor,
        pdf_request.calificacionesIncorrectas,
        pdf_request.calificacionesCorrectas,
        pdf_request.motivo,
        pdf_request.academia,
        pdf_request.nombreCoordinador,
    )
    
    return FileResponse(pdf_file_path, media_type='application/pdf', filename="output.pdf", status_code=201)

@app.get("/api/matricula/{email}", response_model=str, dependencies=[Depends(verify_auth_token)])
async def getEmployeeId(email: str):
    response = getEmployeeIdByEmail(email)

    if response is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return response