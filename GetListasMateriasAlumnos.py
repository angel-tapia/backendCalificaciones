import re
import json

# Function to parse a given text file and extract the relevant information
def parse_class_list_v7(file_content):
    json_data = []
    
    # Adjusted regex pattern to account for leading spaces and accented characters
    subject_pattern = re.compile(r'^\s*A2024\s+FACULTAD\sDE\sCIENCIAS\sF[IÍ]SICO\sMATEM[ÁA]T\s+(\d+)\s+(.+?)\s+\d+\s+\S+$')
    student_pattern = re.compile(r'^\s*(\d)\s+(\d+)\s+(.+)$')
    
    lines = file_content.splitlines()
    current_class = None
    
    for line in lines:
        # Detect if the line contains subject information
        subject_match = subject_pattern.match(line)
        student_match = student_pattern.match(line)
        
        if subject_match:
            #print(f"Detected subject line: {line}")
            # Clean the subject name to remove trailing numbers or extra content
            raw_subject_name = subject_match.group(2).strip()
            cleaned_subject_name = re.sub(r'\s*\d+$', '', raw_subject_name)  # Remove trailing numbers
            
            # Save the previous class if it exists before starting a new one
            if current_class:
                json_data.append(current_class)
                
            # Start a new class entry
            current_class = {
                "ClaveMateria": subject_match.group(1),
                "NombreMateria": cleaned_subject_name,
                "Grupo": line.split()[-1][-3:] if len(line.split()[-1]) > 3 else line.split()[-1],# Last non-whitespace block should be the group code
                "Alumnos": []
            }
        
        elif student_match and current_class:
            # Add student information to the current class
            alumno = {
                "Oportunidad": student_match.group(1),
                "Matricula": student_match.group(2),
                "Nombre": student_match.group(3).strip(),
            }
            current_class["Alumnos"].append(alumno)
    
    # Append the last class if it exists
    if current_class:
        json_data.append(current_class)
    
    #print(f"Parsed data: {json_data}")
    return json_data

# Load and parse each text file with the adjusted parsing logic
file_paths = ['/Users/angel/Downloads/Listas 420.txt', '/Users/angel/Downloads/Listas 430.txt', '/Users/angel/Downloads/Listas 440.txt']  # Replace with your local file paths

parsed_data_by_file_v7 = {}

for file_path in file_paths:
    print(f"Processing file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        parsed_data_by_file_v7[file_path] = parse_class_list_v7(file_content)

# Output the parsed data (you can save it to a file if needed)
for file, data in parsed_data_by_file_v7.items():
    output_file = file.replace('.txt', '.json')
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"JSON file created: {output_file}")
