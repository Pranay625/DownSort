import main
from pathlib import Path
import shutil

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

def save_files(move_instructions: list):

    for action in move_instructions:
        src_path = Path(action["src"])
        dest_path = Path(action["dest"])

        dest_path.parent.mkdir(parents = True, exist_ok = True)

        shutil.move(str(src_path), str(dest_path))

    return True

