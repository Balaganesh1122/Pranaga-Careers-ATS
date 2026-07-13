from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.application import (
    JobApplicationCreate,
    JobApplicationResponse,
)
from app.services.application.application_service import (
    ApplicationService,
)

router = APIRouter(
    prefix="/api/candidate",
    tags=["Job Applications"],
)


@router.post(
    "/apply",
    response_model=JobApplicationResponse,
    status_code=201,
)
def apply_job(
    application: JobApplicationCreate,
    db: Session = Depends(get_db),
):

    try:

        return ApplicationService.apply_job(
            db,
            application,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )