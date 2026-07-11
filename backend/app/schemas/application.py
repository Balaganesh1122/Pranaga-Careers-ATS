from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ApplicationBase(BaseModel):
    candidate_id: int
    job_id: int

    work_authorization: bool

    notice_period: Optional[str] = None

    internship_available: Optional[bool] = None

    privacy_consent: bool


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationResponse(ApplicationBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)