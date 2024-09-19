import pandas as pd
import json

# Load the Excel file
file_path = '/Users/angel/Desktop/Angel/9no Semestre/Servicio Social/Horarios_Maestros_AD2024.xlsx'  # Update this with the correct path to your file
excel_data = pd.read_excel(file_path)

# Clean up any leading/trailing whitespace from columns
excel_data.columns = excel_data.columns.str.strip()

# Initialize variables to hold the parsed data
result = []
current_professor = None

# Function to map 'Modalidad' values
def map_modalidad(modalidad_value):
    if pd.isnull(modalidad_value):
        return ''
    modalidad_value = int(modalidad_value)
    if modalidad_value == 1:
        return '420'
    elif modalidad_value == 4:
        return '430'
    elif modalidad_value == 5:
        return '440'
    return str(modalidad_value)

# Iterate over the rows in the dataframe
for index, row in excel_data.iterrows():
    clave = str(row['Clave']).strip()  # Extract and strip the 'Clave' column
    nombre = str(row['Nombre']).strip() if pd.notnull(row['Nombre']) else ''  # Safely extract and strip 'Nombre'

    # If 'Clave' is numeric and more than 5 characters, it's a professor
    if len(clave) > 4:
        # Save the current professor's data before moving to the next one
        if current_professor is not None:
            result.append(current_professor)
        
        # Initialize a new professor
        current_professor = {
            "EmployeeId": clave,
            "NombreMaestro": nombre,
            "Materias": []
        }
    elif current_professor is not None: 
        if clave == 'nan':
            continue
        materia = {
            "ClaveMateria": clave.upper(),
            "NombreMateria": nombre,
            "Grupo": str(row['Grupo']).strip(),
            "Plan": map_modalidad(row['Modalidad']).strip(),
            "Academia": str(row['Academia']).strip()
        }
        if materia not in current_professor['Materias']:
          current_professor['Materias'].append(materia)

# Add the last professor to the result
if current_professor is not None:
    result.append(current_professor)


# Output the JSON to a file
output_file = '/Users/angel/Desktop/Angel/9no Semestre/backendCalificaciones/app/data/professors_subjects.json'
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)

print(f"JSON data has been written to {output_file}")