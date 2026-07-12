from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.resume_data import ResumeData
from app.ai.parser.parser_service import ParserService
from app.models.application import Application
from app.models.job import Job
from app.ai.ats.scorer import ATSScorer
from app.models.ats_result import ATSResult
from app.ai.parser.information_extractor import (
    ResumeInformationExtractor,
)


class AIEvaluationService:

    @staticmethod
    def evaluate_application(
        db: Session,
        application_id: int,
    ):
        """
        AI Evaluation Pipeline

        Stage 1 -> Find Resume
        Stage 2 -> Parse Resume
        Stage 3 -> Extract Candidate Information
        """

        # ---------------------------------
        # Stage 1 - Find Resume
        # ---------------------------------

        resume = (
            db.query(ResumeData)
            .filter(
                ResumeData.application_id == application_id
            )
            .first()
        )

        if not resume:
            raise HTTPException(
                status_code=404,
                detail="Resume not found."
            )

        # ---------------------------------
        # Stage 2 - Parse Resume
        # ---------------------------------

        resume_text = ParserService.extract_resume_text(
            resume.file_path
        )

        # Save parsed text into database (optional but recommended)
        if not resume.parsed_text:
            resume.parsed_text = resume_text
            db.commit()
            db.refresh(resume)

        # ---------------------------------
        # Stage 3 - Extract Candidate Information
        # ---------------------------------

        candidate_information = (
            ResumeInformationExtractor.extract(
                resume_text
            )
        )
        # ---------------------------------
        # Stage 4 - Fetch Application
        # ---------------------------------

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

        # ---------------------------------
        # Stage 4 - Fetch Job
        # ---------------------------------

        job = (
            db.query(Job)
            .filter(Job.id == application.job_id)
            .first()
        )

        if not job:
            raise HTTPException(
                status_code=404,
                detail="Job not found."
            )
        # ---------------------------------
        # Stage 5 - ATS Score Calculation
        # ---------------------------------

        candidate_skills = candidate_information.get(
            "skills",
            []
        )

        job_skills = job.required_skills or []

        ats_result = ATSScorer.calculate(
            candidate_skills,
            job_skills,
        )

        # ---------------------------------
        # Stage 6 - Save ATS Result
        # ---------------------------------

        existing_result = (
            db.query(ATSResult)
            .filter(
                ATSResult.application_id == application_id
            )
            .first()
        )

        if existing_result:

            existing_result.ats_score = ats_result["ats_score"]
            existing_result.matching_skills = ats_result["matched_skills"]
            existing_result.missing_skills = ats_result["missing_skills"]
            existing_result.ai_summary = ats_result["summary"]
            existing_result.recommendation = ats_result["recommendation"]

        else:

            existing_result = ATSResult(
                application_id=application_id,
                ats_score=ats_result["ats_score"],
                matching_skills=ats_result["matched_skills"],
                missing_skills=ats_result["missing_skills"],
                ai_summary=ats_result["summary"],
                recommendation=ats_result["recommendation"],
            )

            db.add(existing_result)

        db.commit()
        db.refresh(existing_result)
        # ---------------------------------
        # Return Result
        # ---------------------------------

        return {
            "resume": resume.file_name,
            "candidate": candidate_information,
            "job": {
                "title": job.title,
                "department": job.department,
                "required_skills": job.required_skills,
            },
            "ats": ats_result,
            "saved_result_id": existing_result.id,
        }