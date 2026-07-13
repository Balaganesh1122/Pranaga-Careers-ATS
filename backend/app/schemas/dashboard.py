from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class DashboardSummary(BaseModel):

    total_jobs: int
    active_jobs: int
    total_candidates: int
    total_applications: int
    average_ats_score: float

    applied: int
    shortlisted: int
    under_review: int
    interview: int
    rejected: int
    offered: int
    hired: int


class RecruiterApplication(BaseModel):

    application_id: int
    candidate_id: int
    candidate_name: str

    job_id: int
    job_title: str

    ats_score: Optional[float] = None
    recommendation: Optional[str] = None

    status: str
    created_at: datetime


class ResumeInfo(BaseModel):

    file_name: Optional[str] = None
    extracted_email: Optional[str] = None
    extracted_phone: Optional[str] = None
    extracted_skills: List[str] = []


class ATSInfo(BaseModel):

    ats_score: Optional[float] = None
    recommendation: Optional[str] = None
    summary: Optional[str] = None

    matching_skills: List[str] = []
    missing_skills: List[str] = []


class ApplicationInfo(BaseModel):

    application_id: int
    job_title: str
    status: str
    applied_on: datetime


class CandidateDetails(BaseModel):

    id: int

    first_name: str
    middle_name: Optional[str] = None
    last_name: str

    email: str
    phone: str

    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None

    highest_education: Optional[str] = None
    years_of_experience: Optional[float] = None

    current_company: Optional[str] = None
    current_designation: Optional[str] = None

    expected_ctc: Optional[float] = None
    current_ctc: Optional[float] = None

    notice_period: Optional[str] = None

    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None

    resume: ResumeInfo
    ats: ATSInfo
    application: ApplicationInfo

from typing import Literal


class ApplicationStatusUpdate(BaseModel):

    status: Literal[
        "Applied",
        "Under Review",
        "Shortlisted",
        "Interview Scheduled",
        "Interview Completed",
        "On Hold",
        "Rejected",
        "Offer Extended",
        "Hired",
    ]