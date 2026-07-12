from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.job import Job
from app.models.application import Application
from app.models.ats_result import ATSResult


class DashboardService:

    @staticmethod
    def get_dashboard_summary(db: Session):

        total_jobs = db.query(Job).count()

        total_applications = db.query(Application).count()

        average_score = (
            db.query(func.avg(ATSResult.ats_score))
            .scalar()
        )

        shortlisted = (
            db.query(Application)
            .filter(
                Application.status == "Shortlisted"
            )
            .count()
        )

        under_review = (
            db.query(Application)
            .filter(
                Application.status == "Under Review"
            )
            .count()
        )

        rejected = (
            db.query(Application)
            .filter(
                Application.status == "Rejected"
            )
            .count()
        )

        return {

            "total_jobs": total_jobs,

            "total_applications": total_applications,

            "average_ats_score": round(
                average_score or 0,
                2,
            ),

            "shortlisted": shortlisted,

            "under_review": under_review,

            "rejected": rejected,

        }