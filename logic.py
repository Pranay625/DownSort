import data
import main
import hashlib
from pathlib import Path

def inspect_files(raw_files: list) -> dict:

    """
    Takes the list of file dictionaries and counts how many files
    exist for each extension type
    """

    report = {}

    for file_record in raw_files:
        ext = file_record["extension"]

        if ext in report:
            report[ext] += 1
        else:
            report[ext] = 1

    return report


def organize_files(raw_files: list, base_path_str: str) -> list:

    CATEGORY_MAPPING = {
        "pdf": "Docs",
        "docx": "Docs",
        "txt": "Docs", 
        "png": "Img", 
        "jpg": "Img",
        "jpeg": "Img",
        "zip": "Archive",
        "tar": "Archive"
    }

    instructions = []

    base_path = Path(base_path_str)

    for file_record in raw_files:
        ext = file_record["extension"]
        filename= file_record["name"]
        current_abs_path = file_record["absolute_path"]

        category_folder = CATEGORY_MAPPING.get(ext, "Others")

        dest_abs_path = str(base_path / category_folder / filename)
        if current_abs_path == dest_abs_path:
            continue

        instructions.append({
            "src": current_abs_path,
            "dest": dest_abs_path
        })

    return instructions


def find_duplicate(raw_files):

    size_tracker = []
    duplicates = []

    for file_record in raw_files:

        size = file_record["size_bytes"]
        path = file_record["absolute_path"]

        if size in size_tracker:
            size_tracker[size].append(path)
        else:
            size_tracker[size] = [path]

    for size, path in size_tracker.items():
        if len(path) > 1:
            duplicates[size] = path

    return duplicates