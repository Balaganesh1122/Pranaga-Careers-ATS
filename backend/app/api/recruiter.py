from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.recruiter.recruiter_service import RecruiterService
from app.services.recruiter.dashboard_service import DashboardService
from app.services.recruiter.recruiter_note_service import RecruiterNoteService

from app.schemas.recruiter import (
    DashboardResponse,
    RecruiterApplicationResponse,
    RecruiterApplicationDetailsResponse,
    TopCandidateResponse,
    UpdateApplicationStatusRequest,
    UpdateApplicationStatusResponse,
    RecruiterNoteCreate,
    RecruiterNoteResponse,
    RecruiterNoteListResponse,
    RecruiterNoteDeleteResponse,
)

from app.services.recruiter.interview_service import InterviewService

from app.schemas.recruiter import (
    InterviewCreate,
    InterviewUpdate,
    InterviewResponse,
    InterviewListResponse,
    InterviewDeleteResponse,
    InterviewFeedbackRequest,
)
from app.services.auth.dependencies import (
    get_current_recruiter,
)

from app.models.user import User
from app.services.auth.dependencies import get_current_recruiter
from app.models.user import User
from app.schemas.dashboard import CandidateDetails
from app.services.email.email_log_service import EmailLogService




router = APIRouter(
    prefix="/api/recruiter",
    tags=["Recruiter"],
)


# -------------------------------------------------
# Dashboard
# -------------------------------------------------

@router.get(
    "/dashboard",
    response_model=DashboardResponse,
)
def recruiter_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_recruiter),
):
    return DashboardService.get_dashboard_summary(db)


# -------------------------------------------------
# Applications
# -------------------------------------------------

@router.get(
    "/applications",
    response_model=List[RecruiterApplicationResponse],
)
def get_all_applications(
    page: int = 1,
    page_size: int = 10,
    job_id: int | None = None,
    status: str | None = None,
    search: str | None = None,
    sort_by: str = "ats_score",
    sort_order: str = "desc",
    db: Session = Depends(get_db),
):
    return RecruiterService.get_all_applications(
        db=db,
        page=page,
        page_size=page_size,
        job_id=job_id,
        status=status,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
    )


@router.get(
    "/applications/{application_id}",
    response_model=RecruiterApplicationDetailsResponse,
)
def get_application_details(
    application_id: int,
    db: Session = Depends(get_db),
):
    return RecruiterService.get_application_details(
        db=db,
        application_id=application_id,
    )


@router.patch(
    "/applications/{application_id}/status",
    response_model=UpdateApplicationStatusResponse,
)
def update_application_status(
    application_id: int,
    request: UpdateApplicationStatusRequest,
    db: Session = Depends(get_db),
):
    return RecruiterService.update_application_status(
        db=db,
        application_id=application_id,
        status=request.status,
    )


# -------------------------------------------------
# Top Candidates
# -------------------------------------------------

@router.get(
    "/top-candidates",
    response_model=List[TopCandidateResponse],
)
def get_top_candidates(
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return RecruiterService.get_top_candidates(
        db=db,
        limit=limit,
    )


# -------------------------------------------------
# Recruiter Notes
# -------------------------------------------------

@router.post(
    "/applications/{application_id}/notes",
    response_model=RecruiterNoteResponse,
)
def add_recruiter_note(
    application_id: int,
    request: RecruiterNoteCreate,
    db: Session = Depends(get_db),
):
    return RecruiterNoteService.add_note(
        db=db,
        application_id=application_id,
        request=request,
    )


@router.get(
    "/applications/{application_id}/notes",
    response_model=RecruiterNoteListResponse,
)
def get_recruiter_notes(
    application_id: int,
    db: Session = Depends(get_db),
):
    return RecruiterNoteService.get_notes(
        db=db,
        application_id=application_id,
    )


@router.delete(
    "/notes/{note_id}",
    response_model=RecruiterNoteDeleteResponse,
)
def delete_recruiter_note(
    note_id: int,
    db: Session = Depends(get_db),
):
    return RecruiterNoteService.delete_note(
        db=db,
        note_id=note_id,
    )

@router.post(
    "/applications/{application_id}/interviews",
    response_model=InterviewResponse,
)
def schedule_interview(
    application_id: int,
    request: InterviewCreate,
    db: Session = Depends(get_db),
):

    return InterviewService.schedule_interview(
        db=db,
        application_id=application_id,
        request=request,
    )

@router.get(
    "/interviews",
    response_model=InterviewListResponse,
)
def get_all_interviews(
    db: Session = Depends(get_db),
):

    return InterviewService.get_all_interviews(
        db=db,
    )

@router.get(
    "/interviews/{interview_id}",
    response_model=InterviewResponse,
)
def get_interview(
    interview_id: int,
    db: Session = Depends(get_db),
):

    return InterviewService.get_interview(
        db=db,
        interview_id=interview_id,
    )

@router.put(
    "/interviews/{interview_id}",
    response_model=InterviewResponse,
)
def update_interview(
    interview_id: int,
    request: InterviewUpdate,
    db: Session = Depends(get_db),
):

    return InterviewService.update_interview(
        db=db,
        interview_id=interview_id,
        request=request,
    )

@router.put(
    "/interviews/{interview_id}/feedback",
    response_model=InterviewResponse,
)
def submit_interview_feedback(

    interview_id: int,

    request: InterviewFeedbackRequest,

    db: Session = Depends(get_db),
):

    return InterviewService.submit_feedback(

        db=db,

        interview_id=interview_id,

        feedback=request.feedback,

        rating=request.rating,

    )

@router.delete(
    "/interviews/{interview_id}",
    response_model=InterviewDeleteResponse,
)
def delete_interview(
    interview_id: int,
    db: Session = Depends(get_db),
):

    return InterviewService.delete_interview(
        db=db,
        interview_id=interview_id,
    )

@router.get(
    "/candidate/{candidate_id}",
    response_model=CandidateDetails,
)
def recruiter_candidate_details(
    candidate_id: int,
    db: Session = Depends(get_db),
):

    return DashboardService.get_candidate_details(
        db,
        candidate_id,
    )

@router.get("/email-logs")
def get_email_logs(
    db: Session = Depends(get_db),
):

    return EmailLogService.get_all_logs(db)