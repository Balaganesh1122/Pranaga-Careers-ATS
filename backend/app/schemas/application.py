from datetime import datetime
from pydantic import BaseModel, ConfigDict


# ============================================================
# Existing ATS
# ============================================================

class ApplicationCreate(BaseModel):
    candidate_id: int
    job_id: int


# ============================================================
# Candidate Apply
# ============================================================

class JobApplicationCreate(BaseModel):

    candidate_id: int

    job_id: int

    work_authorization: bool

    privacy_consent: bool

    notice_period: str | None = None

    internship_available: bool | None = None


# ============================================================
# Response
# ============================================================

class JobApplicationResponse(BaseModel):

    id: int

    candidate_id: int

    job_id: int

    status: str

    work_authorization: bool

    privacy_consent: bool

    notice_period: str | None = None

    internship_available: bool | None = None

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)