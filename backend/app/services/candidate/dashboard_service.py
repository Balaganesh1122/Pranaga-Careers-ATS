from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.models.application import Application
from app.models.interview import Interview

from app.schemas.candidate_dashboard import (
    CandidateInterview,
    CandidateInterviewList,
)

from fastapi import HTTPException


class CandidateDashboardService:

    @staticmethod
    def get_my_interviews(
        db: Session,
        user,
    ):

        candidate = (
            db.query(Candidate)
            .filter(
                Candidate.email == user.email
            )
            .first()
        )

        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found."
            )

        interviews = (
            db.query(
                Interview,
                Application,
            )
            .join(
                Application,
                Interview.application_id == Application.id,
            )
            .filter(
                Application.candidate_id == candidate.id,
            )
            .order_by(
                Interview.interview_date.desc(),
                Interview.interview_time.desc(),
            )
            .all()
        )

        result = []

        for interview, application in interviews:

            result.append(

                CandidateInterview(

                    interview_id=interview.id,

                    application_id=application.id,

                    interview_type=interview.interview_type,

                    interview_round=interview.interview_round,

                    interviewer_name=interview.interviewer_name,

                    interviewer_email=interview.interviewer_email,

                    interview_date=interview.interview_date,

                    interview_time=interview.interview_time,

                    meeting_link=interview.meeting_link,

                    location=interview.location,

                    status=interview.status,

                    feedback=interview.feedback,

                    rating=interview.rating,

                )

            )

        return CandidateInterviewList(

            interviews=result

        )