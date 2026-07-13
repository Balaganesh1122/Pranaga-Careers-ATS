from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.public import (
    PublicJobListResponse,
    PublicJobDetailsResponse,
)
from app.services.public.jobs_service import PublicJobsService

router = APIRouter(
    prefix="/api/v1/public",
    tags=["Public Careers"],
)


@router.get(
    "/jobs",
    response_model=PublicJobListResponse,
)
def get_public_jobs(
    page: int = 1,
    page_size: int = 10,
    search: str | None = None,
    department: str | None = None,
    location: str | None = None,
    employment_type: str | None = None,
    work_mode: str | None = None,
    db: Session = Depends(get_db),
):

    return PublicJobsService.get_jobs(
        db=db,
        page=page,
        page_size=page_size,
        search=search,
        department=department,
        location=location,
        employment_type=employment_type,
        work_mode=work_mode,
    )


@router.get(
    "/jobs/{job_id}",
    response_model=PublicJobDetailsResponse,
)
def get_job_details(
    job_id: int,
    db: Session = Depends(get_db),
):

    job = PublicJobsService.get_job_details(
        db=db,
        job_id=job_id,
    )

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    return job