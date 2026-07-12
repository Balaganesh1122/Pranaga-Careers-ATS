from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.candidate import (
    CandidateCreate,
    CandidateUpdate,
    CandidateResponse,
)
from app.services.candidate.candidate_service import CandidateService
from app.services.auth.dependencies import get_current_candidate
from app.models.user import User


router = APIRouter(
    prefix="/api/candidates",
    tags=["Candidates"]
)


@router.get("/", response_model=list[CandidateResponse])
def get_candidates(db: Session = Depends(get_db)):
    return CandidateService.get_all_candidates(db)


@router.get("/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = CandidateService.get_candidate_by_id(db, candidate_id)

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate


@router.post("/", response_model=CandidateResponse, status_code=201)
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):
    return CandidateService.create_candidate(db, candidate)


@router.put("/{candidate_id}", response_model=CandidateResponse)
def update_candidate(
    candidate_id: int,
    candidate: CandidateUpdate,
    db: Session = Depends(get_db)
):
    updated = CandidateService.update_candidate(
        db,
        candidate_id,
        candidate
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return updated


@router.delete("/{candidate_id}")
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    deleted = CandidateService.delete_candidate(db, candidate_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return {"message": "Candidate deleted successfully"}