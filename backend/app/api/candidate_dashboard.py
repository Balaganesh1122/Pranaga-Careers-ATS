from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.auth.dependencies import get_current_candidate
from app.models.user import User

from app.services.candidate.dashboard_service import CandidateDashboardService
from app.schemas.candidate_dashboard import CandidateInterviewList


router = APIRouter(
    prefix="/api/candidate",
    tags=["Candidate Dashboard"],
)


@router.get(
    "/interviews",
    response_model=CandidateInterviewList,
)
def get_my_interviews(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_candidate),
):

    return CandidateDashboardService.get_my_interviews(
        db=db,
        user=current_user,
    )