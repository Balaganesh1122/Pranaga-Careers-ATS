from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.models.application import Application
from app.services.email.email_service import EmailService

class ApplicationSubmissionService:

    @staticmethod
    def submit_application(
        db: Session,
        request,
    ):
        # Step 1 - Find existing candidate
        candidate = (
            db.query(Candidate)
            .filter(Candidate.email == request.email)
            .first()
        )

        # Step 2 - Create candidate if not found
        if not candidate:
            candidate = Candidate(
                full_name=request.full_name,
                email=request.email,
                phone=request.phone,
                linkedin_url=request.linkedin_url,
                github_url=request.github_url,
                portfolio_url=request.portfolio_url,
            )

            db.add(candidate)
            db.commit()
            db.refresh(candidate)

        # Step 3 - Create application
        application = Application(
            candidate_id=candidate.id,
            job_id=request.job_id,
            work_authorization=request.work_authorization,
            notice_period=request.notice_period,
            internship_available=request.internship_available,
            privacy_consent=request.privacy_consent,
        )

        db.add(application)
        db.commit()
        db.refresh(application)

        return {
            "success": True,
            "message": "Application submitted successfully.",
            "candidate_id": candidate.id,
            "application_id": application.id,
        }
    


