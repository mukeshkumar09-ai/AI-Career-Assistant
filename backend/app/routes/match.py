from fastapi import APIRouter
from app.utils.match_score import calculate_match_score

router = APIRouter()

@router.post("/match-resume-jd")
async def match_resume_jd(data: dict):

    resume_skills = data.get("resume_skills", [])
    jd_skills = data.get("jd_skills", [])

    result = calculate_match_score(
        resume_skills,
        jd_skills
    )

    return result