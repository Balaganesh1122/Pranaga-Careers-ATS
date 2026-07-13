import os
import shutil

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.ai.parser.parser_service import ParserService
from app.ai.parser.information_extractor import ResumeInformationExtractor
from app.models.resume_data import ResumeData


class ResumeUploadService:

    UPLOAD_DIR = "uploads/resumes"

    @staticmethod
    def upload_resume(
        db: Session,
        candidate_id: int,
        file: UploadFile,
    ):

        # ----------------------------------------------------
        # Validate Extension
        # ----------------------------------------------------

        extension = os.path.splitext(file.filename)[1].lower()

        if extension not in [".pdf", ".docx"]:
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are allowed.",
            )

        # ----------------------------------------------------
        # Create Upload Folder
        # ----------------------------------------------------

        os.makedirs(
            ResumeUploadService.UPLOAD_DIR,
            exist_ok=True,
        )

        # ----------------------------------------------------
        # Save File
        # ----------------------------------------------------

        file_path = os.path.join(
            ResumeUploadService.UPLOAD_DIR,
            f"{candidate_id}_{file.filename}",
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ----------------------------------------------------
        # Parse Resume
        # ----------------------------------------------------

        parsed_text = ParserService.extract_resume_text(
            file_path
        )

        extracted = ResumeInformationExtractor.extract(
            parsed_text
        )

        # ----------------------------------------------------
        # Convert Skills
        # ----------------------------------------------------

        skills = extracted.get("skills", [])

        # ----------------------------------------------------
        # Check Existing Resume
        # ----------------------------------------------------

        resume = (
            db.query(ResumeData)
            .filter(
                ResumeData.candidate_id == candidate_id
            )
            .first()
        )

        if resume is None:

            resume = ResumeData(
                candidate_id=candidate_id,
            )

            db.add(resume)

        # ----------------------------------------------------
        # Save Data
        # ----------------------------------------------------

        resume.file_name = file.filename
        resume.file_path = file_path
        resume.file_size = os.path.getsize(file_path)
        resume.mime_type = file.content_type

        resume.parsed_text = parsed_text

        resume.extracted_name = extracted.get("name")
        resume.extracted_email = extracted.get("email")
        resume.extracted_phone = extracted.get("phone")
        resume.extracted_skills = ",".join(skills)

        db.commit()
        db.refresh(resume)

        return {
            "candidate_id": candidate_id,
            "file_name": resume.file_name,
            "extracted_name": resume.extracted_name,
            "extracted_email": resume.extracted_email,
            "extracted_phone": resume.extracted_phone,
            "extracted_skills": skills,
            "message": "Resume uploaded successfully.",
        }