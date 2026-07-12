from pprint import pprint

from app.ai.ats.scorer import ATSScorer

candidate_skills = [
    "Python",
    "SQL",
    "Docker",
    "Git",
    "AWS",
    "React",
]

job_skills = [
    "Python",
    "SQL",
    "Docker",
    "TensorFlow",
    "FastAPI",
    "Git",
]

result = ATSScorer.calculate(
    candidate_skills,
    job_skills,
)

pprint(result)