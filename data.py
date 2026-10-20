import main.py
from pathlib import Path

def load_files(data_link):

    path = Path(data_link)
    list_of_files = []

    # 1. Validation check
    # If not a folder
    if not path.is_dir():
        return None

    
    for item in path.iterdir():

        if item.is_file():

            file_info = {
                "name": item.name,
                "absolute_path": str(item.resolve()),
                # Extracting extension
                "extension": item.suffix.lower().replace(".", ""),
                "size_bytes": item.stat().st_size
            }

            # Handle files that don't have an extension
            if not file_info["extension"]:

                file_info["extension"] = "no_extension"

            list_of_files.append(file_info) 


    return list_of_files

def save_files(path_to_change):

    




