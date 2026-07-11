from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate
from app.core.logger import logger

class JobService:

    @staticmethod
    def get_all_jobs(db: Session):
        return db.query(Job).all()

    @staticmethod
    def get_job_by_id(db: Session, job_id: int):
        return db.query(Job).filter(Job.id == job_id).first()

    @staticmethod
    def create_job(db: Session, job: JobCreate):

        db_job = Job(
            title=job.title,
            department=job.department,
            location=job.location,
            employment_type=job.employment_type,
            experience=job.experience,
            education=job.education,
            description=job.description,
            responsibilities=job.responsibilities,
            required_skills=job.required_skills,
            preferred_skills=job.preferred_skills
        )

        db.add(db_job)
        db.commit()
        db.refresh(db_job)

        return db_job

    @staticmethod
    def update_job(db: Session, job_id: int, job: JobUpdate):

        db_job = db.query(Job).filter(Job.id == job_id).first()

        if not db_job:
            return None

        update_data = job.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_job, key, value)

        db.commit()
        db.refresh(db_job)

        return db_job

    @staticmethod
    def delete_job(db: Session, job_id: int):

        db_job = db.query(Job).filter(Job.id == job_id).first()

        if not db_job:
            return False

        db.delete(db_job)
        db.commit()

        return True