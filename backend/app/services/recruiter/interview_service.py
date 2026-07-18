from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.application import Application
from app.models.interview import Interview
from app.models.candidate import Candidate
from app.models.job import Job

from app.services.email.email_service import EmailService

from app.schemas.recruiter import (
    InterviewCreate,
    InterviewUpdate,
    InterviewResponse,
    InterviewListResponse,
    InterviewDeleteResponse,
)


class InterviewService:

    @staticmethod
    def schedule_interview(
        db: Session,
        application_id: int,
        request: InterviewCreate,
    ):

        application = (
            db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        interview = Interview(

            application_id=application_id,

            interview_type=request.interview_type,

            interview_round=request.interview_round,

            interviewer_name=request.interviewer_name,

            interviewer_email=request.interviewer_email,

            interview_date=request.interview_date,

            interview_time=request.interview_time,

            meeting_link=request.meeting_link,

            location=request.location,

            status="Scheduled",

            feedback=None,

            rating=None,
        )

        db.add(interview)

        db.commit()

        db.refresh(interview)

        # =====================================================
        # Send Interview Email
        # =====================================================

        try:

            candidate = (
                db.query(Candidate)
                .filter(Candidate.id == application.candidate_id)
                .first()
            )

            job = (
                db.query(Job)
                .filter(Job.id == application.job_id)
                .first()
            )

            EmailService.send_template_email(
                db=db,
                application_id=application.id,
                to_email=candidate.email,
                subject="Interview Scheduled - Pranaga Solutions",
                template_name="interview.html",
                email_type="Interview",
                context={
                    "candidate_name": f"{candidate.first_name} {candidate.last_name}",
                    "job_title": job.title,
                    "company_name": "Pranaga Solutions",
                    "interview_date": request.interview_date,
                    "interview_time": request.interview_time,
                    "interviewer_name": request.interviewer_name,
                    "meeting_link": request.meeting_link,
                    "location": request.location,
                },
            )

        except Exception as e:

            print(f"Interview email failed: {e}")

        return InterviewResponse.model_validate(interview)

    @staticmethod
    def get_all_interviews(db: Session):

        interviews = (
            db.query(Interview)
            .order_by(
                Interview.interview_date,
                Interview.interview_time,
            )
            .all()
        )

        return InterviewListResponse(

            interviews=[

                InterviewResponse.model_validate(i)

                for i in interviews

            ]
        )

    @staticmethod
    def get_interview(
        db: Session,
        interview_id: int,
    ):

        interview = (
            db.query(Interview)
            .filter(
                Interview.id == interview_id
            )
            .first()
        )

        if not interview:
            raise HTTPException(
                status_code=404,
                detail="Interview not found."
            )

        return InterviewResponse.model_validate(interview)

    @staticmethod
    def update_interview(
        db: Session,
        interview_id: int,
        request: InterviewUpdate,
    ):

        interview = (
            db.query(Interview)
            .filter(
                Interview.id == interview_id
            )
            .first()
        )

        if not interview:
            raise HTTPException(
                status_code=404,
                detail="Interview not found."
            )

        update_data = request.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():

            setattr(interview, key, value)

        db.commit()

        db.refresh(interview)

        return InterviewResponse.model_validate(interview)

    @staticmethod
    def delete_interview(
        db: Session,
        interview_id: int,
    ):

        interview = (
            db.query(Interview)
            .filter(
                Interview.id == interview_id
            )
            .first()
        )

        if not interview:
            raise HTTPException(
                status_code=404,
                detail="Interview not found."
            )

        db.delete(interview)

        db.commit()

        return InterviewDeleteResponse(

            message="Interview deleted successfully."

        )

    @staticmethod
    def submit_feedback(
        db: Session,
        interview_id: int,
        feedback: str,
        rating: float,
    ):

        interview = (
            db.query(Interview)
            .filter(
                Interview.id == interview_id
            )
            .first()
        )

        if not interview:
            raise HTTPException(
                status_code=404,
                detail="Interview not found."
            )

        interview.feedback = feedback

        interview.rating = rating

        interview.status = "Completed"

        db.commit()

        db.refresh(interview)

        return InterviewResponse.model_validate(interview)