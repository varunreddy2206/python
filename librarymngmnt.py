import json
import os

library_file= 'library_data.json'

def load_library():
    if not os.path.exists(library_file):
        return{}
    try:
        with open(library_file,'r') as file:
            return json.load(file)
    except Exception as e:
        print(f'error loading library data: {e}')
        return{}
    
def save_library():
    try:
        with open(library_file,'w') as file:
            json.dump(file,)
        
    except Exception as e:
        print(f'error saving library data')