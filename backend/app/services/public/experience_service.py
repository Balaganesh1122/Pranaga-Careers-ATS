from sqlalchemy.orm import Session

from app.models.job import Job


class ExperienceService:

    @staticmethod
    def get_experiences(db: Session):

        experiences = (
            db.query(Job.experience)
            .filter(Job.is_active == True)
            .distinct()
            .order_by(Job.experience)
            .all()
        )

        return [
            {
                "experience": row.experience
            }
            for row in experiences
        ]