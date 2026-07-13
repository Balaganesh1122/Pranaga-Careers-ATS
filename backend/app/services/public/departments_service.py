from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.job import Job


class DepartmentService:

    @staticmethod
    def get_departments(db: Session):

        departments = (
            db.query(
                Job.department,
                func.count(Job.id).label("open_positions")
            )
            .filter(Job.is_active == True)
            .group_by(Job.department)
            .order_by(Job.department)
            .all()
        )

        return [
            {
                "name": row.department,
                "open_positions": row.open_positions,
            }
            for row in departments
        ]