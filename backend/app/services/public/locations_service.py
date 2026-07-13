from sqlalchemy.orm import Session

from app.models.job import Job


class LocationService:

    @staticmethod
    def get_locations(db: Session):

        locations = (
            db.query(Job.location)
            .filter(Job.is_active == True)
            .distinct()
            .order_by(Job.location)
            .all()
        )

        return [
            {
                "location": row.location
            }
            for row in locations
        ]