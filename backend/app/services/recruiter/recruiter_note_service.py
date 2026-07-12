from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.application import Application
from app.models.recruiter_note import RecruiterNote

from app.schemas.recruiter import (
    RecruiterNoteCreate,
    RecruiterNoteResponse,
    RecruiterNoteListResponse,
    RecruiterNoteDeleteResponse,
)


class RecruiterNoteService:

    @staticmethod
    def add_note(
        db: Session,
        application_id: int,
        request: RecruiterNoteCreate,
    ):

        application = (
            db.query(Application)
            .filter(
                Application.id == application_id
            )
            .first()
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        note = RecruiterNote(
            application_id=application_id,
            note=request.note,
        )

        db.add(note)
        db.commit()
        db.refresh(note)

        return RecruiterNoteResponse.model_validate(note)

    @staticmethod
    def get_notes(
        db: Session,
        application_id: int,
    ):

        application = (
            db.query(Application)
            .filter(
                Application.id == application_id
            )
            .first()
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail="Application not found."
            )

        notes = (
            db.query(RecruiterNote)
            .filter(
                RecruiterNote.application_id == application_id
            )
            .order_by(
                RecruiterNote.created_at.desc()
            )
            .all()
        )

        return RecruiterNoteListResponse(
            notes=[
                RecruiterNoteResponse.model_validate(note)
                for note in notes
            ]
        )

    @staticmethod
    def delete_note(
        db: Session,
        note_id: int,
    ):

        note = (
            db.query(RecruiterNote)
            .filter(
                RecruiterNote.id == note_id
            )
            .first()
        )

        if not note:
            raise HTTPException(
                status_code=404,
                detail="Recruiter note not found."
            )

        db.delete(note)
        db.commit()

        return RecruiterNoteDeleteResponse(
            message="Recruiter note deleted successfully."
        )