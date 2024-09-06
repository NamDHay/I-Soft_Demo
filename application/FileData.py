import json
from pathlib import Path
class FileData:
    def read(self, file):
        with open(file, 'r') as openfile:
            json_object = json.load(openfile)
            json_object = json.dumps(json_object)
        return json_object

    def write(self, file_path, entry):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            print("Error: JSON decode error. The file may be corrupted.")
            return
        data.append(entry)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            
    def list_files_in_directory(self, directory_path):
        path = Path(directory_path)
        if path.exists() and path.is_dir():
            files = [f for f in path.iterdir() if f.is_file()]
            return [f.name for f in files]
        else:
            print(f"The directory '{directory_path}' does not exist or is not a directory.")
            return []