def calculate_match_score(resume_skills, jd_skills):

    matched = list(set(resume_skills) & set(jd_skills))

    missing = list(set(jd_skills) - set(resume_skills))

    if len(jd_skills) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_skills)) * 100)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }