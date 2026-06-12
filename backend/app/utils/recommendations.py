SKILL_RECOMMENDATIONS = {
    "Docker": "Learn Docker and containerization basics",
    "AWS": "Learn EC2, S3, IAM and deployment",
    "React": "Build a frontend application using React",
    "FastAPI": "Build REST APIs using FastAPI",
    "Kubernetes": "Learn Pods, Deployments and Services"
}

def get_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:
        if skill in SKILL_RECOMMENDATIONS:
            recommendations.append(
                SKILL_RECOMMENDATIONS[skill]
            )

    return recommendations