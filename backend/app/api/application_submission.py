from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.application_submission import (
    ApplicationSubmissionRequest,
)
from app.services.application_submission.service import (
    ApplicationSubmissionService,
)

router = APIRouter(
    prefix="/api/application-submission",
    tags=["Application Submission"],
)


@router.post("/submit")
def submit_application(
    request: ApplicationSubmissionRequest,
    db: Session = Depends(get_db),
):
    return ApplicationSubmissionService.submit_application(
        db,
        request,
    )