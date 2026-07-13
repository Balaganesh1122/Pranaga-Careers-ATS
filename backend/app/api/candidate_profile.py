from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.candidate_profile import (
    CandidateProfileResponse,
    CandidateProfileUpdate,
)
from app.services.candidate.profile_service import (
    CandidateProfileService,
)

router = APIRouter(
    prefix="/api/candidate/profile",
    tags=["Candidate Profile"],
)


@router.get(
    "/{candidate_id}",
    response_model=CandidateProfileResponse,
)
def get_candidate_profile(
    candidate_id: int,
    db: Session = Depends(get_db),
):

    candidate = CandidateProfileService.get_profile(
        db,
        candidate_id,
    )

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found.",
        )

    return candidate


@router.put(
    "/{candidate_id}",
    response_model=CandidateProfileResponse,
)
def update_candidate_profile(
    candidate_id: int,
    profile: CandidateProfileUpdate,
    db: Session = Depends(get_db),
):

    candidate = CandidateProfileService.update_profile(
        db,
        candidate_id,
        profile,
    )

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found.",
        )

    return candidate