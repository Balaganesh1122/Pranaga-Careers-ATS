from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job
from app.models.ats_result import ATSResult
from app.models.resume_data import ResumeData

from app.services.recruiter.filters import RecruiterFilter
from app.services.recruiter.pagination import Pagination

from app.schemas.recruiter import (
    RecruiterApplicationResponse,
    RecruiterApplicationDetailsResponse,
    ResumeResponse,
    TopCandidateResponse,
    UpdateApplicationStatusResponse,
)


class RecruiterService:

    @staticmethod
    def get_all_applications(
        db: Session,
        page: int = 1,
        page_size: int = 10,
        job_id: int | None = None,
        status: str | None = None,
        search: str | None = None,
        sort_by: str = "ats_score",
        sort_order: str = "desc",
    ):

        query = (
            db.query(
                Application,
                Candidate,
                Job,
                ATSResult,
            )
            .join(
                Candidate,
                Application.candidate_id == Candidate.id,
            )
            .join(
                Job,
                Application.job_id == Job.id,
            )
            .outerjoin(
                ATSResult,
                ATSResult.application_id == Application.id,
            )
        )

        query = RecruiterFilter.apply_filters(
            query=query,
            job_id=job_id,
            status=status,
            search=search,
        )

        paginated = Pagination.paginate(
            query=query,
            page=page,
            page_size=page_size,
        )

        applications = []

        for application, candidate, job, ats in paginated["items"]:

            applications.append(
                RecruiterApplicationResponse(

                    application_id=application.id,

                    first_name=candidate.first_name,

                    middle_name=candidate.middle_name,

                    last_name=candidate.last_name,

                    email=candidate.email,

                    job_title=job.title,

                    ats_score=ats.ats_score if ats else 0,

                    recommendation=ats.recommendation if ats else "Not Evaluated",

                    status=application.status,

                    applied_at=application.created_at,
                )
            )

        return applications

    @staticmethod
    def get_application_details(
        db: Session,
        application_id: int,
    ):

        result = (
            db.query(
                Application,
                Candidate,
                Job,
                ATSResult,
                ResumeData,
            )
            .join(
                Candidate,
                Application.candidate_id == Candidate.id,
            )
            .join(
                Job,
                Application.job_id == Job.id,
            )
            .outerjoin(
                ATSResult,
                ATSResult.application_id == Application.id,
            )
            .outerjoin(
                ResumeData,
                ResumeData.application_id == Application.id,
            )
            .filter(
                Application.id == application_id
            )
            .first()
        )

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        application, candidate, job, ats, resume = result

        resume_response = None

        if resume:
            resume_response = ResumeResponse(
                id=resume.id,
                file_name=resume.file_name,
                download_url=f"/api/resume/download/{resume.id}",
            )

        return RecruiterApplicationDetailsResponse(

                application_id=application.id,

                first_name=candidate.first_name,

                middle_name=candidate.middle_name,

                last_name=candidate.last_name,

                email=candidate.email,

                phone=candidate.phone,

                linkedin_url=candidate.linkedin_url,

                github_url=candidate.github_url,

                portfolio_url=candidate.portfolio_url,

                resume=resume_response,

                job_title=job.title,

                department=job.department,

                application_status=application.status,

                ats_score=ats.ats_score if ats else 0,

                matched_skills=ats.matching_skills if ats else [],

                missing_skills=ats.missing_skills if ats else [],

                recommendation=ats.recommendation if ats else "Not Evaluated",

                ai_summary=ats.ai_summary if ats else "",

                applied_at=application.created_at,
            )

    @staticmethod
    def update_application_status(
        db: Session,
        application_id: int,
        status: str,
    ):

        application = (
            db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        old_status = application.status

        application.status = status

        db.commit()
        db.refresh(application)

        return UpdateApplicationStatusResponse(
            message="Application status updated successfully.",
            application_id=application.id,
            old_status=old_status,
            new_status=application.status,
        )

    @staticmethod
    def get_top_candidates(
        db: Session,
        limit: int = 10,
    ):

        results = (
            db.query(
                Application,
                Candidate,
                Job,
                ATSResult,
            )
            .join(
                Candidate,
                Application.candidate_id == Candidate.id,
            )
            .join(
                Job,
                Application.job_id == Job.id,
            )
            .join(
                ATSResult,
                ATSResult.application_id == Application.id,
            )
            .order_by(
                ATSResult.ats_score.desc()
            )
            .limit(limit)
            .all()
        )

        candidates = []

        for application, candidate, job, ats in results:

            candidates.append(
                TopCandidateResponse(
                    application_id=application.id,
                    first_name=candidate.first_name,

                    middle_name=candidate.middle_name,

                    last_name=candidate.last_name,
                    email=candidate.email,
                    job_title=job.title,
                    ats_score=ats.ats_score,
                    recommendation=ats.recommendation,
                )
            )

        return candidates