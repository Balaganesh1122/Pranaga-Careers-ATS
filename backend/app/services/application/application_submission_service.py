from sqlalchemy.orm import Session

from app.services.candidate.candidate_service import CandidateService
from app.services.application.application_service import ApplicationService

from app.schemas.application_submit import (
    ApplicationSubmissionRequest,
)


class ApplicationSubmissionService:

    @staticmethod
    def submit_application(
        db: Session,
        request: ApplicationSubmissionRequest,
    ):

        # Step 1
        candidate = CandidateService.create_candidate(
            db,
            request.candidate,
        )

        # Step 2
        application = ApplicationService.create_application(
            db,
            candidate.id,
            request.application,
        )

        # Step 3
        return {
            "success": True,
            "message": "Application submitted successfully.",
            "data": {
                "candidate_id": candidate.id,
                "application_id": application.id,
                "status": application.status,
            },
        }