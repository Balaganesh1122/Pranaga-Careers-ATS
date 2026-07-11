from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.job import JobCreate, JobUpdate, JobResponse
from app.services.jobs.job_service import JobService

router = APIRouter(
    prefix="/api/jobs",
    tags=["Jobs"]
)


@router.get("/", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return JobService.get_all_jobs(db)


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = JobService.get_job_by_id(db, job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


@router.post("/", response_model=JobResponse, status_code=201)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return JobService.create_job(db, job)


@router.put("/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    job: JobUpdate,
    db: Session = Depends(get_db)
):
    updated_job = JobService.update_job(db, job_id, job)

    if not updated_job:
        raise HTTPException(status_code=404, detail="Job not found")

    return updated_job


@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    deleted = JobService.delete_job(db, job_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "message": "Job deleted successfully"
    }