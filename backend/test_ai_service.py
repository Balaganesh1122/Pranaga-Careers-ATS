from pprint import pprint

from app.core.database import SessionLocal
from app.services.ai_evaluation.ai_evaluation_service import (
    AIEvaluationService,
)

db = SessionLocal()

result = AIEvaluationService.evaluate_application(
    db=db,
    application_id=1,
)

print("\n========== Resume ==========\n")
print(result["resume"])

print("\n========== Candidate ==========\n")
pprint(result["candidate"])

print("\n========== Job ==========\n")
pprint(result["job"])

print("\n========== ATS Result ==========\n")
pprint(result["ats"])