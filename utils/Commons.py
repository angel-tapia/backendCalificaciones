import json

# Load the JSON data from the specified file
def load_json_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)
    
