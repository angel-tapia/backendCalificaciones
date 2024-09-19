from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from datetime import date

from models.alumno import Alumno
from models.materia import MateriaAlumnos
from models.profesor import Profesor

def generate_pdf(alumno: Alumno,
                 materiaAlumno: MateriaAlumnos,
                 plan: str,
                 profesor: Profesor,
                 calificacionIncorrecta: str,
                 calificacionCorrecta: str,
                 motivo: str,
                 academia: str,
                 nombreCoordinador: str) -> str:
    file_path = "change_request.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Header Information
    header_style = ParagraphStyle(name='HeaderStyle', fontSize=12, leading=14)
    elements.append(Paragraph("M.C. MARIA AURORA CHAVEZ VALDEZ", header_style))
    elements.append(Paragraph("Jefa del Departamento Escolar", header_style))
    elements.append(Paragraph("Facultad de Ciencias Físico Matemáticas", header_style))
    elements.append(Paragraph("Presente.-", header_style))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Por medio de la presente me permito solicitar un cambio de calificación debido a un error involuntario.", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Course Information
    course_data = [
        ["Materia:", f"{materiaAlumno.NombreMateria}"],
        ["Clave:", f"{materiaAlumno.ClaveMateria}"],
        ["Gpo.:", f"{materiaAlumno.Grupo}"],
        ["Plan:", f"{plan}"],
    ]
    course_table = Table(course_data, colWidths=[1 * inch, 3 * inch])
    course_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    elements.append(course_table)
    elements.append(Spacer(1, 12))

    # Exam Type
    if alumno.Oportunidad == '1' or alumno.Oportunidad == '3' or alumno.Oportunidad == '5':
      elements.append(Paragraph("Tipo Examen:      ORD.      X          EXT.", styles['Normal']))
    else: 
      elements.append(Paragraph("Tipo Examen:      ORD.        EXT.   X", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Motivo
    motivo_data = [["Motivo:", f"{motivo}"]]
    motivo_table = Table(motivo_data, colWidths=[1 * inch, 5 * inch])
    motivo_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    elements.append(motivo_table)
    elements.append(Spacer(1, 12))

    # Grades Information
    grades_data = [
        ["Matrícula", "Nombre", "Calificación Incorrecta (capturada en SIASE)", "Calificación Correcta"],
        [f"{alumno.Matricula}", f"{alumno.Nombre[:30]}", f"{calificacionIncorrecta}", f"{calificacionCorrecta}"],
        ["", "", "", ""],  # Empty rows
        ["", "", "", ""],
        ["", "", "", ""]
    ]
    grades_table = Table(grades_data, colWidths=[1 * inch, 2.5 * inch, 3 * inch, 1.5 * inch])
    grades_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    elements.append(grades_table)
    elements.append(Spacer(1, 12))

    # Footer
    footer = Paragraph("Agradeciendo de antemano esta solicitud quedo de Usted, para cualquier aclaración o duda al respecto.", styles['Normal'])
    elements.append(footer)
    elements.append(Spacer(1, 12))

    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    today = date.today()
    footer_info = [
        ["ATENTAMENTE.-", "Vo. Bo."],
        [f"San Nicolás de los Garza, N.L. a {today.day} de {months[today.month - 1]} de {today.year}"]
    ]
    footer_table = Table(footer_info, colWidths=[4.5 * inch, 2 * inch])
    footer_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    elements.append(footer_table)
    
    # Signatures
    elements.append(Spacer(1, 48))
    signature_info = [
        [profesor.NombreMaestro, "             ", nombreCoordinador],
        [""],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    signature_table = Table(signature_info, colWidths=[2 * inch, 2 * inch, 2 * inch])
    signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    elements.append(signature_table)
    
    # Build the PDF
    doc.build(elements)
    return file_path