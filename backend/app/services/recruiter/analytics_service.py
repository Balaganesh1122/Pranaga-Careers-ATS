from sqlalchemy import func, extract
from sqlalchemy.orm import Session

from app.models.job import Job
from app.models.application import Application
from app.models.ats_result import ATSResult

from app.schemas.analytics import (
    AnalyticsOverview,
    StatusChartItem,
    ATSDistributionItem,
    JobAnalyticsItem,
    MonthlyApplicationsItem,
)


class AnalyticsService:

    # ==========================================================
    # Dashboard Overview
    # ==========================================================

    @staticmethod
    def get_overview(db: Session):

        total_jobs = db.query(Job).count()

        active_jobs = (
            db.query(Job)
            .filter(Job.is_active == True)
            .count()
        )

        total_applications = db.query(Application).count()

        average_ats = (
            db.query(func.avg(ATSResult.ats_score))
            .scalar()
            or 0
        )

        return AnalyticsOverview(

            total_jobs=total_jobs,

            active_jobs=active_jobs,

            total_applications=total_applications,

            average_ats_score=round(float(average_ats), 2),

            applied=db.query(Application).filter(
                Application.status == "Applied"
            ).count(),

            under_review=db.query(Application).filter(
                Application.status == "Under Review"
            ).count(),

            shortlisted=db.query(Application).filter(
                Application.status == "Shortlisted"
            ).count(),

            interview=db.query(Application).filter(
                Application.status == "Interview"
            ).count(),

            rejected=db.query(Application).filter(
                Application.status == "Rejected"
            ).count(),

            offered=db.query(Application).filter(
                Application.status == "Offered"
            ).count(),

            hired=db.query(Application).filter(
                Application.status == "Hired"
            ).count(),
        )

    # ==========================================================
    # Status Chart
    # ==========================================================

    @staticmethod
    def get_status_chart(db: Session):

        rows = (
            db.query(
                Application.status,
                func.count(Application.id),
            )
            .group_by(Application.status)
            .all()
        )

        return [
            StatusChartItem(
                status=status,
                count=count,
            )
            for status, count in rows
        ]

    # ==========================================================
    # ATS Distribution
    # ==========================================================

    @staticmethod
    def get_ats_distribution(db: Session):

        scores = (
            db.query(ATSResult.ats_score)
            .all()
        )

        buckets = {
            "90-100": 0,
            "80-89": 0,
            "70-79": 0,
            "60-69": 0,
            "<60": 0,
        }

        for (score,) in scores:

            if score >= 90:
                buckets["90-100"] += 1

            elif score >= 80:
                buckets["80-89"] += 1

            elif score >= 70:
                buckets["70-79"] += 1

            elif score >= 60:
                buckets["60-69"] += 1

            else:
                buckets["<60"] += 1

        return [
            ATSDistributionItem(
                range=key,
                count=value,
            )
            for key, value in buckets.items()
        ]

    # ==========================================================
    # Applications Per Job
    # ==========================================================

    @staticmethod
    def get_job_statistics(db: Session):

        rows = (
            db.query(
                Job.title,
                func.count(Application.id),
            )
            .outerjoin(
                Application,
                Job.id == Application.job_id,
            )
            .group_by(Job.title)
            .all()
        )

        return [
            JobAnalyticsItem(
                job_title=title,
                applications=count,
            )
            for title, count in rows
        ]

    # ==========================================================
    # Monthly Applications
    # ==========================================================

    @staticmethod
    def get_monthly_applications(db: Session):

        rows = (
            db.query(
                extract("month", Application.created_at),
                func.count(Application.id),
            )
            .group_by(
                extract("month", Application.created_at)
            )
            .order_by(
                extract("month", Application.created_at)
            )
            .all()
        )

        months = {
            1: "Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun",
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec",
        }

        return [
            MonthlyApplicationsItem(
                month=months.get(int(month), str(month)),
                applications=count,
            )
            for month, count in rows
        ]