from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


# -----------------------------
# Base Schema
# -----------------------------
class JobBase(BaseModel):
    title: str
    department: str
    location: str
    employment_type: str
    experience: str
    education: str
    description: str
    responsibilities: List[str]
    required_skills: List[str]
    preferred_skills: Optional[List[str]] = []


# -----------------------------
# Create Job
# -----------------------------
class JobCreate(JobBase):
    pass


# -----------------------------
# Update Job
# -----------------------------
class JobUpdate(BaseModel):
    title: Optional[str] = None
    department: Optional[str] = None
    location: Optional[str] = None
    employment_type: Optional[str] = None
    experience: Optional[str] = None
    education: Optional[str] = None
    description: Optional[str] = None
    responsibilities: Optional[List[str]] = None
    required_skills: Optional[List[str]] = None
    preferred_skills: Optional[List[str]] = None


# -----------------------------
# Response Schema
# -----------------------------
class JobResponse(JobBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)