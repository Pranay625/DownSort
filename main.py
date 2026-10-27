from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import data
import logic

app = FastAPI(title="Smart Downloads Organizer API")

class OrganizerRequest(BaseModel):
    path: str

@app.get("/inspect")
def inspect_files(path: str):
    file_data = data.load_files(path)
    if file_data is None:
        raise HTTPException(status_code=400, detail="Invalid directory path.")
    return logic.inspect_files(file_data)

@app.put("/organize")
def organize_files(req: OrganizerRequest):
    file_data = data.load_files(req.path)
    if file_data is None:
        raise HTTPException(status_code=400, detail="Invalid directory path.")

    instructions = logic.organize_files(file_data, req.path)
    if instructions:
        data.save_files(instructions)
    return {"message": f"Successfully organized {len(instructions)} files!", "instructions": instructions}

@app.get("/duplicates")
def find_duplicates(path: str):
    file_data = data.load_files(path)
    if file_data is None:
        raise HTTPException(status_code=400, detail="Invalid directory path.")
    return logic.find_duplicate(file_data)