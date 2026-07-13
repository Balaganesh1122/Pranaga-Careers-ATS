from pydantic import BaseModel, EmailStr
from typing import Optional


class CandidateProfileUpdate(BaseModel):

    first_name: str

    middle_name: Optional[str] = None

    last_name: str

    phone: str

    country: str

    state: str

    city: str

    highest_education: str

    years_of_experience: float

    current_company: Optional[str] = None

    current_designation: Optional[str] = None

    linkedin_url: Optional[str] = None

    github_url: Optional[str] = None

    portfolio_url: Optional[str] = None

    expected_ctc: Optional[float] = None

    current_ctc: Optional[float] = None

    notice_period: Optional[str] = None


class CandidateProfileResponse(BaseModel):

    first_name: str

    middle_name: Optional[str]

    last_name: str

    email: EmailStr

    phone: str

    country: str

    state: str

    city: str

    highest_education: str

    years_of_experience: float

    current_company: Optional[str]

    current_designation: Optional[str]

    linkedin_url: Optional[str]

    github_url: Optional[str]

    portfolio_url: Optional[str]

    expected_ctc: Optional[float]

    current_ctc: Optional[float]

    notice_period: Optional[str]