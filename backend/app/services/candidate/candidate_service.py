from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateUpdate


class CandidateService:

    @staticmethod
    def get_all_candidates(db: Session):
        return db.query(Candidate).all()

    @staticmethod
    def get_candidate_by_id(db: Session, candidate_id: int):
        return db.query(Candidate).filter(
            Candidate.id == candidate_id
        ).first()

    @staticmethod
    def get_candidate_by_email(db: Session, email: str):
        return db.query(Candidate).filter(
            Candidate.email == email
        ).first()

    @staticmethod
    def create_candidate(db: Session, candidate: CandidateCreate):

        existing = CandidateService.get_candidate_by_email(
            db,
            candidate.email
        )

        if existing:
            return existing

        db_candidate = Candidate(
            first_name=candidate.first_name,
            middle_name=candidate.middle_name,
            last_name=candidate.last_name,
            email=candidate.email,
            phone=candidate.phone,
            linkedin_url=candidate.linkedin_url,
            github_url=candidate.github_url,
            portfolio_url=candidate.portfolio_url
        )

        db.add(db_candidate)
        db.commit()
        db.refresh(db_candidate)

        return db_candidate

    @staticmethod
    def update_candidate(
        db: Session,
        candidate_id: int,
        candidate: CandidateUpdate
    ):

        db_candidate = CandidateService.get_candidate_by_id(
            db,
            candidate_id
        )

        if not db_candidate:
            return None

        update_data = candidate.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_candidate, key, value)

        db.commit()
        db.refresh(db_candidate)

        return db_candidate

    @staticmethod
    def delete_candidate(db: Session, candidate_id: int):

        db_candidate = CandidateService.get_candidate_by_id(
            db,
            candidate_id
        )

        if not db_candidate:
            return False

        db.delete(db_candidate)
        db.commit()

        return True