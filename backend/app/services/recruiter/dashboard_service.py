from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.job import Job
from app.models.application import Application
from app.models.ats_result import ATSResult
from app.models.candidate import Candidate
from app.models.candidate import Candidate
from app.models.resume_data import ResumeData


class DashboardService:

    @staticmethod
    def get_dashboard_summary(db: Session):

        # ---------------------------------------
        # Jobs
        # ---------------------------------------

        total_jobs = db.query(Job).count()

        active_jobs = (
            db.query(Job)
            .filter(Job.is_active == True)
            .count()
        )

        # ---------------------------------------
        # Candidates
        # ---------------------------------------

        total_candidates = (
            db.query(Candidate)
            .count()
        )

        # ---------------------------------------
        # Applications
        # ---------------------------------------

        total_applications = (
            db.query(Application)
            .count()
        )

        # ---------------------------------------
        # ATS Score
        # ---------------------------------------

        average_score = (
            db.query(func.avg(ATSResult.ats_score))
            .scalar()
        )

        # ---------------------------------------
        # Application Status
        # ---------------------------------------

        applied = (
            db.query(Application)
            .filter(Application.status == "Applied")
            .count()
        )

        shortlisted = (
            db.query(Application)
            .filter(Application.status == "Shortlisted")
            .count()
        )

        under_review = (
            db.query(Application)
            .filter(Application.status == "Under Review")
            .count()
        )

        interview = (
            db.query(Application)
            .filter(Application.status == "Interview")
            .count()
        )

        rejected = (
            db.query(Application)
            .filter(Application.status == "Rejected")
            .count()
        )

        offered = (
            db.query(Application)
            .filter(Application.status == "Offer")
            .count()
        )

        hired = (
            db.query(Application)
            .filter(Application.status == "Hired")
            .count()
        )

        return {

            "total_jobs": total_jobs,

            "active_jobs": active_jobs,

            "total_candidates": total_candidates,

            "total_applications": total_applications,

            "average_ats_score": round(
                average_score or 0,
                2,
            ),

            "applied": applied,

            "shortlisted": shortlisted,

            "under_review": under_review,

            "interview": interview,

            "rejected": rejected,

            "offered": offered,

            "hired": hired,
        }
    
    @staticmethod
    def get_applications(db: Session):

        applications = (
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
            .order_by(
                Application.created_at.desc()
            )
            .all()
        )

        results = []

        for application, candidate, job, ats in applications:

            full_name = " ".join(
                filter(
                    None,
                    [
                        candidate.first_name,
                        candidate.middle_name,
                        candidate.last_name,
                    ],
                )
            )

            results.append({

                "application_id": application.id,

                "candidate_id": candidate.id,

                "candidate_name": full_name,

                "job_id": job.id,

                "job_title": job.title,

                "ats_score": ats.ats_score if ats else None,

                "recommendation": ats.recommendation if ats else None,

                "status": application.status,

                "created_at": application.created_at,
            })

        return results
    @staticmethod
    def get_candidate_details(
        db: Session,
        candidate_id: int,
    ):

        candidate = (
            db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

        if not candidate:
            raise ValueError("Candidate not found.")

        application = (
            db.query(Application)
            .filter(
                Application.candidate_id == candidate_id
            )
            .order_by(Application.created_at.desc())
            .first()
        )

        if not application:
            raise ValueError("Application not found.")

        job = (
            db.query(Job)
            .filter(Job.id == application.job_id)
            .first()
        )

        resume = (
            db.query(ResumeData)
            .filter(
                ResumeData.candidate_id == candidate_id
            )
            .first()
        )

        ats = (
            db.query(ATSResult)
            .filter(
                ATSResult.application_id == application.id
            )
            .first()
        )

        skills = []

        if resume and resume.extracted_skills:

            if isinstance(resume.extracted_skills, str):

                skills = [
                    x.strip()
                    for x in resume.extracted_skills.split(",")
                    if x.strip()
                ]

            else:

                skills = resume.extracted_skills

        return {

            "id": candidate.id,

            "first_name": candidate.first_name,

            "middle_name": candidate.middle_name,

            "last_name": candidate.last_name,

            "email": candidate.email,

            "phone": candidate.phone,

            "country": candidate.country,

            "state": candidate.state,

            "city": candidate.city,

            "highest_education": candidate.highest_education,

            "years_of_experience": candidate.years_of_experience,

            "current_company": candidate.current_company,

            "current_designation": candidate.current_designation,

            "expected_ctc": candidate.expected_ctc,

            "current_ctc": candidate.current_ctc,

            "notice_period": candidate.notice_period,

            "linkedin_url": candidate.linkedin_url,

            "github_url": candidate.github_url,

            "portfolio_url": candidate.portfolio_url,

            "resume": {

                "file_name": resume.file_name if resume else None,

                "extracted_email": resume.extracted_email if resume else None,

                "extracted_phone": resume.extracted_phone if resume else None,

                "extracted_skills": skills,
            },

            "ats": {

                "ats_score": ats.ats_score if ats else None,

                "recommendation": ats.recommendation if ats else None,

                "summary": ats.ai_summary if ats else None,

                "matching_skills": ats.matching_skills if ats else [],

                "missing_skills": ats.missing_skills if ats else [],
            },

            "application": {

                "application_id": application.id,

                "job_title": job.title,

                "status": application.status,

                "applied_on": application.created_at,
            },
        }
    
        @staticmethod
        def update_application_status(
            db: Session,
            application_id: int,
            status: str,
        ):

            application = (
                db.query(Application)
                .filter(
                    Application.id == application_id
                )
                .first()
            )

            if not application:
                raise ValueError("Application not found.")

            application.status = status

            db.commit()

            db.refresh(application)

            return {

                "message": "Application status updated successfully.",

                "application_id": application.id,

                "status": application.status,
            }
        
        