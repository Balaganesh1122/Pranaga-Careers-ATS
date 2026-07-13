from sqlalchemy.orm import Session

from app.models.job import Job


class WorkModeService:

    @staticmethod
    def get_work_modes(db: Session):

        work_modes = (
            db.query(Job.work_mode)
            .filter(Job.is_active == True)
            .distinct()
            .order_by(Job.work_mode)
            .all()
        )

        return [
            {
                "work_mode": row.work_mode
            }
            for row in work_modes
        ]