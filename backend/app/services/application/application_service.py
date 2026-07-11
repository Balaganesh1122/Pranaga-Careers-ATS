from sqlalchemy.orm import Session

from app.models.application import Application
from app.schemas.application import ApplicationCreate


class ApplicationService:

    @staticmethod
    def create_application(
        db: Session,
        candidate_id: int,
        application: ApplicationCreate,
    ):

        db_application = Application(
            candidate_id=candidate_id,
            job_id=application.job_id,
            work_authorization=application.work_authorization,
            notice_period=application.notice_period,
            internship_available=application.internship_available,
            privacy_consent=application.privacy_consent,
        )

        db.add(db_application)
        db.commit()
        db.refresh(db_application)

        return db_application