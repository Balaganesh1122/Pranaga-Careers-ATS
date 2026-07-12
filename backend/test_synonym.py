from pprint import pprint

from app.ai.ats.scorer import ATSScorer

candidate = [
    "ML",
    "Postgres",
    "Containerization",
    "GitHub",
    "RESTful APIs"
]

job = [
    "Machine Learning",
    "PostgreSQL",
    "Docker",
    "Git",
    "REST API"
]

result = ATSScorer.calculate(
    candidate,
    job,
)

pprint(result)