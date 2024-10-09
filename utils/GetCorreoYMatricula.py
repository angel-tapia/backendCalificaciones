import pandas as pd
import json

# Load the spreadsheet
file_path = '/Users/angel/Desktop/Angel/9no Semestre/Servicio Social/DOCENTES ACTIVOS AGO-DIC 2024_correoYnombre.xlsx'
spreadsheet = pd.ExcelFile(file_path)

# Load the second sheet and skip initial rows
second_sheet_df = spreadsheet.parse(spreadsheet.sheet_names[1], skiprows=3)
second_sheet_df.columns = ["EmployeeId", "EmployeeName", "EmployeeEmail"]

# Convert EmployeeId to string
second_sheet_df["EmployeeId"] = second_sheet_df["EmployeeId"].astype(str)
second_sheet_df["EmployeeEmail"] = second_sheet_df["EmployeeEmail"].str.lower()

# Select only the necessary columns
json_data = second_sheet_df[["EmployeeId", "EmployeeEmail"]].dropna().to_dict(orient="records")

# Define the output file path
output_file_path = '/Users/angel/Desktop/Angel/9no Semestre/backendCalificaciones/data/EmployeeEmails.json'

# Write the JSON data to the file
with open(output_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON file saved as {output_file_path}")
