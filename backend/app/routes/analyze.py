from fastapi import APIRouter
from app.utils.extract_jd_skills import extract_jd_skills
from app.utils.match_score import calculate_match_score
from app.utils.recommendations import get_recommendations

router = APIRouter()

@router.post("/analyze-resume")
async def analyze_resume(data: dict):

    # Get data from request
    resume_skills = data.get("resume_skills", [])
    jd_text = data.get("jd_text", "")

    # Extract skills from JD
    jd_skills = extract_jd_skills(jd_text)

    # Calculate match score
    result = calculate_match_score(
        resume_skills,
        jd_skills
    )

    # Generate recommendations
    recommendations = list(set(
    get_recommendations(
        result["missing_skills"]
    )
    ))
    

    # Return final response
    return {
        "match_score": result["match_score"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"],
        "recommendations": recommendations
    }