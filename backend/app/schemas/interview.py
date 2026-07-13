from datetime import date, time, datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class InterviewCreate(BaseModel):

    application_id: int

    interview_type: str

    interview_round: str

    interviewer_name: str

    interviewer_email: Optional[EmailStr] = None

    interview_date: date

    interview_time: time

    meeting_link: Optional[str] = None

    location: Optional[str] = None


class InterviewResponse(BaseModel):

    id: int

    application_id: int

    interview_type: str

    interview_round: str

    interviewer_name: str

    interviewer_email: Optional[str]

    interview_date: date

    interview_time: time

    meeting_link: Optional[str]

    location: Optional[str]

    status: str

    feedback: Optional[str]

    rating: Optional[float]

    created_at: datetime

    class Config:
        from_attributes = True