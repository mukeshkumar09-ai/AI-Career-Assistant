from fastapi import APIRouter, UploadFile, File
import fitz
import os

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    pdf = fitz.open(file_path)

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return {
        "resume_text": text
    }