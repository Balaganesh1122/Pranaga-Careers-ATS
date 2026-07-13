from datetime import date, time
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class CandidateInterview(BaseModel):

    interview_id: int

    application_id: int

    interview_type: str

    interview_round: str

    interviewer_name: str

    interviewer_email: Optional[str] = None

    interview_date: date

    interview_time: time

    meeting_link: Optional[str] = None

    location: Optional[str] = None

    status: str

    feedback: Optional[str] = None

    rating: Optional[float] = None

    model_config = ConfigDict(
        from_attributes=True
    )


class CandidateInterviewList(BaseModel):

    interviews: List[CandidateInterview]

    model_config = ConfigDict(
        from_attributes=True
    )