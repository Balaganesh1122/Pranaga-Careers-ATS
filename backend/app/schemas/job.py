from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


# -----------------------------
# Base Schema
# -----------------------------
class JobBase(BaseModel):
    title: str
    department: str
    location: str
    employment_type: str
    work_mode: str
    experience: str
    education: str

    openings: int

    salary_range: str | None = None

    description: str

    responsibilities: List[str]

    required_skills: List[str]

    preferred_skills: List[str] = []

    nice_to_have_skills: List[str] = []

    application_deadline: datetime | None = None

    is_active: bool = True


# -----------------------------
# Create Job
# -----------------------------
class JobCreate(JobBase):
    pass


# -----------------------------
# Update Job
# -----------------------------
class JobUpdate(BaseModel):

    title: str | None = None

    department: str | None = None

    location: str | None = None

    employment_type: str | None = None

    work_mode: str | None = None

    experience: str | None = None

    education: str | None = None

    openings: int | None = None

    salary_range: str | None = None

    description: str | None = None

    responsibilities: List[str] | None = None

    required_skills: List[str] | None = None

    preferred_skills: List[str] | None = None

    nice_to_have_skills: List[str] | None = None

    application_deadline: datetime | None = None

    is_active: bool | None = None


# -----------------------------
# Response
# -----------------------------
class JobResponse(JobBase):

    id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )