from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job
from app.models.ats_result import ATSResult

class RecruiterFilter:

    @staticmethod
    def apply(
        query,
        *,
        job_id=None,
        status=None,
        search=None,
        sort_by="ats_score",
        sort_order="desc",
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
            query = query.filter(
                Candidate.full_name.ilike(f"%{search}%")
            )

        if sort_by == "ats_score":

            if sort_order == "desc":
                query = query.order_by(
                    ATSResult.ats_score.desc()
                )
            else:
                query = query.order_by(
                    ATSResult.ats_score.asc()
                )

        elif sort_by == "name":

            query = query.order_by(
                Candidate.full_name.asc()
            )

        elif sort_by == "job":

            query = query.order_by(
                Job.title.asc()
            )

        return query