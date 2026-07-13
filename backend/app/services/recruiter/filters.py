from sqlalchemy.orm import Query

from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job


class RecruiterFilter:

    @staticmethod
    def apply_filters(
        query: Query,
        job_id: int | None = None,
        status: str | None = None,
        search: str | None = None,
    ):

        if job_id:
            query = query.filter(
                Application.job_id == job_id
            )

        if status:
            query = query.filter(
                Application.status == status
            )

        if search:
            query = (
                query.join(Candidate)
                .join(Job)
                .filter(
                    (Candidate.first_name.ilike(f"%{search}%")) |
                    (Candidate.last_name.ilike(f"%{search}%")) |
                    (Candidate.email.ilike(f"%{search}%")) |
                    (Job.title.ilike(f"%{search}%"))
                )
            )

        return query