import os

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.models.application import Application
from app.models.resume_data import ResumeData
from app.utils.file_utils import (
    UPLOAD_FOLDER,
    generate_filename,
    ALLOWED_TYPES,
    MAX_FILE_SIZE,
)


class ResumeService:

    @staticmethod
    async def upload_resume(
        db: Session,
        application_id: int,
        file: UploadFile,
    ):
        # Check if the application exists
        application = (
            db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail=f"Application with ID {application_id} not found."
            )

        # Read file
        content = await file.read()

        # Validate MIME type
        if file.content_type not in ALLOWED_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are allowed."
            )

        # Validate file size
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="Maximum allowed file size is 5 MB."
            )

        # Create uploads folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Generate unique filename
        unique_name = generate_filename(file.filename)

        file_path = os.path.join(
            UPLOAD_FOLDER,
            unique_name,
        )

        # Save file
        with open(file_path, "wb") as buffer:
            buffer.write(content)

        # Save metadata in database
        resume = ResumeData(
            application_id=application_id,
            file_name=file.filename,
            file_path=file_path,
            file_size=len(content),
            mime_type=file.content_type,
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return resume