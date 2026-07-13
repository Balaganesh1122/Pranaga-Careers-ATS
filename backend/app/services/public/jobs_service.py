from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.job import Job


class PublicJobsService:

    @staticmethod
    def get_jobs(
        db: Session,
        page: int = 1,
        page_size: int = 10,
        search: str | None = None,
        department: str | None = None,
        location: str | None = None,
        employment_type: str | None = None,
        work_mode: str | None = None,
    ):

        query = db.query(Job).filter(Job.is_active == True)

        if search:
            query = query.filter(
                Job.title.ilike(f"%{search}%")
            )

        if department:
            query = query.filter(
                Job.department == department
            )

        if location:
            query = query.filter(
                Job.location == location
            )

        if employment_type:
            query = query.filter(
                Job.employment_type == employment_type
            )

        if work_mode:
            query = query.filter(
                Job.work_mode == work_mode
            )

        total = query.count()

        jobs = (
            query.order_by(desc(Job.created_at))
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return {
            "jobs": jobs,
            "total": total,
            "page": page,
            "page_size": page_size,
        }

    @staticmethod
    def get_job_details(
        db: Session,
        job_id: int,
    ):

        return (
            db.query(Job)
            .filter(
                Job.id == job_id,
                Job.is_active == True
            )
            .first()
        )