from sqlalchemy.orm import Session

from app.models.email_log import EmailLog


class EmailLogService:

    @staticmethod
    def get_all_logs(db: Session):

        return (
            db.query(EmailLog)
            .order_by(EmailLog.sent_at.desc())
            .all()
        )