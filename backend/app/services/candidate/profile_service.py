from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.schemas.candidate_profile import (
    CandidateProfileUpdate,
)


class CandidateProfileService:

    @staticmethod
    def get_profile(
        db: Session,
        candidate_id: int,
    ):

        return (
            db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

    @staticmethod
    def update_profile(
        db: Session,
        candidate_id: int,
        profile: CandidateProfileUpdate,
    ):

        candidate = (
            db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

        if not candidate:
            return None

        for key, value in profile.model_dump().items():
            setattr(candidate, key, value)

        db.commit()
        db.refresh(candidate)

        return candidate