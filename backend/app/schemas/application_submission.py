from pydantic import BaseModel, EmailStr


class ApplicationSubmissionRequest(BaseModel):
    first_name: str

    middle_name: str | None = None

    last_name: str
    
    email: EmailStr
    phone: str

    linkedin_url: str | None = None
    github_url: str | None = None
    portfolio_url: str | None = None

    job_id: int

    work_authorization: bool
    notice_period: str
    internship_available: bool | None = None

    privacy_consent: bool