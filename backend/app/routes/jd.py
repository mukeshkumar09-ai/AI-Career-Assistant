from fastapi import APIRouter
from app.utils.extract_jd_skills import extract_jd_skills

router = APIRouter()

@router.post("/upload-jd")
async def upload_jd(data: dict):

    jd_text = data.get("jd_text", "")
    skills = extract_jd_skills(jd_text)

    return {
    "required_skills": skills
    }