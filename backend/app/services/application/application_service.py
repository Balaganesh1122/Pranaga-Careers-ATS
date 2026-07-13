from sqlalchemy.orm import Session

from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job

from app.schemas.application import JobApplicationCreate

from app.services.ai_evaluation.ai_evaluation_service import (
    AIEvaluationService,
)


class ApplicationService:

    @staticmethod
    def apply_job(
        db: Session,
        application: JobApplicationCreate,
    ):

        # -----------------------------------------
        # Check Candidate
        # -----------------------------------------

        candidate = (
            db.query(Candidate)
            .filter(
                Candidate.id == application.candidate_id
            )
            .first()
        )

        if not candidate:
            raise ValueError(
                "Candidate not found."
            )

        # -----------------------------------------
        # Check Job
        # -----------------------------------------

        job = (
            db.query(Job)
            .filter(
                Job.id == application.job_id,
                Job.is_active == True,
            )
            .first()
        )

        if not job:
            raise ValueError(
                "Job not found."
            )

        # -----------------------------------------
        # Prevent Duplicate Application
        # -----------------------------------------

        existing = (
            db.query(Application)
            .filter(
                Application.candidate_id == application.candidate_id,
                Application.job_id == application.job_id,
            )
            .first()
        )

        if existing:
            raise ValueError(
                "You have already applied for this job."
            )

        # -----------------------------------------
        # Create Application
        # -----------------------------------------

        new_application = Application(
            candidate_id=application.candidate_id,
            job_id=application.job_id,
            status="Applied",
            work_authorization=application.work_authorization,
            privacy_consent=application.privacy_consent,
            notice_period=application.notice_period,
            internship_available=application.internship_available,
        )

        db.add(new_application)
        db.commit()
        db.refresh(new_application)

        # -----------------------------------------
        # AI Evaluation
        # -----------------------------------------

        try:

            ai_result = AIEvaluationService.evaluate(

                db=db,

                candidate_id=application.candidate_id,

                job_id=application.job_id,

                application_id=new_application.id,
            )

            print("\n========== AI EVALUATION ==========")
            print(ai_result)
            print("===================================\n")

        except Exception as e:

            print(f"AI Evaluation skipped: {e}")

        return new_application