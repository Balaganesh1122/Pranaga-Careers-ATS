from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


# -----------------------------
# Jobs List
# -----------------------------

class PublicJobResponse(BaseModel):
    id: int
    title: str
    department: str
    location: str
    employment_type: str
    work_mode: str
    experience: str
    salary_range: str | None = None
    openings: int
    application_deadline: datetime |None=None

    model_config=ConfigDict(from_attributes=True)


class PublicJobListResponse(BaseModel):
    jobs:list[PublicJobResponse]
    total:int
    page:int
    page_size:int


# -----------------------------
# Job Details
# -----------------------------

class PublicJobDetailsResponse(BaseModel):
    id: int

    title: str

    job_code: str

    department: str

    team: str

    location: str

    employment_type: str

    work_mode: str

    experience: str

    education: str

    minimum_qualification: str

    preferred_qualification: str | None = None

    salary_range: str | None = None

    openings: int

    about_role: str

    description: str

    responsibilities: list[str]

    required_skills: list[str]

    preferred_skills: list[str]

    nice_to_have_skills: list[str]

    benefits: list[str]

    selection_process: list[str]

    application_deadline: datetime | None = None

    job_status: str

    model_config = ConfigDict(from_attributes=True)


# -----------------------------
# Careers Home
# -----------------------------

class HomeDepartmentResponse(BaseModel):
    name:str
    open_positions:int


class FAQResponse(BaseModel):
    question:str
    answer:str


class CareersHomeResponse(BaseModel):

    hero_title:str

    hero_description:str

    departments:list[HomeDepartmentResponse]

    featured_jobs:list[PublicJobResponse]

    faqs:list[FAQResponse]