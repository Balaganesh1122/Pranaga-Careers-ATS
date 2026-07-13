from sqlalchemy.orm import Session

from app.models.job import Job


class EmploymentTypeService:

    @staticmethod
    def get_employment_types(db: Session):

        employment_types = (
            db.query(Job.employment_type)
            .filter(Job.is_active == True)
            .distinct()
            .order_by(Job.employment_type)
            .all()
        )

        return [
            {
                "employment_type": row.employment_type
            }
            for row in employment_types
        ]