from typing import Optional
from utils.Commons import load_json_data

employee_emails = load_json_data('data/EmployeeEmails.json')

def getEmployeeIdByEmail(email: str) -> Optional[str]:
    for employee in employee_emails:
        if employee['EmployeeEmail'] == email:
            return employee['EmployeeId']
    return None
