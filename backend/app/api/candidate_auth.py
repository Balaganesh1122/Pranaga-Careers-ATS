from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import (
    CandidateRegister,
    CandidateLogin,
    AuthResponse,
)
from app.services.auth.candidate_auth_service import CandidateAuthService

router = APIRouter(
    prefix="/api/auth/candidate",
    tags=["Candidate Authentication"],
)


@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=201,
)
def register_candidate(
    candidate: CandidateRegister,
    db: Session = Depends(get_db),
):
    try:
        return CandidateAuthService.register(
            db,
            candidate,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=AuthResponse,
)
def login_candidate(
    credentials: CandidateLogin,
    db: Session = Depends(get_db),
):
    try:
        return CandidateAuthService.login(
            db,
            credentials.email,
            credentials.password,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )