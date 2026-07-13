from datetime import datetime, date, time
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


# ============================================================
# Dashboard
# ============================================================

class DashboardResponse(BaseModel):
    total_jobs: int
    total_applications: int
    average_ats_score: float
    shortlisted: int
    under_review: int
    rejected: int


# ============================================================
# Resume
# ============================================================

class ResumeResponse(BaseModel):
    id: int
    file_name: str
    download_url: str

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# Recruiter Applications
# ============================================================

class RecruiterApplicationResponse(BaseModel):
    application_id: int
    first_name: str

    middle_name: str | None = None

    last_name: str
    
    email: str
    job_title: str
    ats_score: float
    recommendation: str
    status: str
    applied_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class RecruiterApplicationDetailsResponse(BaseModel):
    application_id: int

    first_name: str

    middle_name: str | None = None

    last_name: str
    
    email: str
    phone: str

    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None

    resume: Optional[ResumeResponse] = None

    job_title: str
    department: str

    application_status: str

    ats_score: float

    matched_skills: List[str]

    missing_skills: List[str]

    recommendation: str

    ai_summary: Optional[str] = None

    applied_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# Top Candidates
# ============================================================

class TopCandidateResponse(BaseModel):
    application_id: int
    first_name: str

    middle_name: str | None = None

    last_name: str
    
    email: str
    job_title: str
    ats_score: float
    recommendation: str

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# Update Application Status
# ============================================================

class UpdateApplicationStatusRequest(BaseModel):
    status: str


class UpdateApplicationStatusResponse(BaseModel):
    message: str
    application_id: int
    old_status: str
    new_status: str


# ============================================================
# Recruiter Notes
# ============================================================

class RecruiterNoteCreate(BaseModel):
    note: str


class RecruiterNoteResponse(BaseModel):
    id: int
    application_id: int
    note: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class RecruiterNoteListResponse(BaseModel):
    notes: List[RecruiterNoteResponse]

    model_config = ConfigDict(
        from_attributes=True
    )


class RecruiterNoteDeleteResponse(BaseModel):
    message: str

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# Interview Management
# ============================================================

class InterviewCreate(BaseModel):

    interviewer_name: str

    interviewer_email: Optional[str] = None

    interview_type: str
    # HR / Technical / Managerial / Final

    interview_round: str
    # Round 1 / Round 2 / Final

    interview_date: date

    interview_time: time

    meeting_link: Optional[str] = None

    location: Optional[str] = None

class InterviewUpdate(BaseModel):

    interviewer_name: Optional[str] = None

    interviewer_email: Optional[str] = None

    interview_type: Optional[str] = None

    interview_round: Optional[str] = None

    interview_date: Optional[date] = None

    interview_time: Optional[time] = None

    meeting_link: Optional[str] = None

    location: Optional[str] = None

    status: Optional[str] = None

    feedback: Optional[str] = None

    rating: Optional[float] = None


class InterviewFeedbackRequest(BaseModel):

    feedback: str

    rating: float


class InterviewResponse(BaseModel):

    id: int

    application_id: int

    interviewer_name: str

    interviewer_email: Optional[str] = None

    interview_type: str

    interview_round: str

    interview_date: date

    interview_time: time

    meeting_link: Optional[str] = None

    location: Optional[str] = None

    status: str

    feedback: Optional[str] = None

    rating: Optional[float] = None

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class InterviewListResponse(BaseModel):

    interviews: List[InterviewResponse]

    model_config = ConfigDict(
        from_attributes=True
    )


class InterviewDeleteResponse(BaseModel):

    message: str

    model_config = ConfigDict(
        from_attributes=True
    )