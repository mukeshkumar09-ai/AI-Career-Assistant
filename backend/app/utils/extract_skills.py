from app.utils.skills import SKILLS_DB

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS_DB:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills