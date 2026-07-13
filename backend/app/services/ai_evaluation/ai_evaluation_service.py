from sqlalchemy.orm import Session

from app.models.resume_data import ResumeData
from app.models.job import Job

from app.ai.ats.skill_matcher import SkillMatcher
from app.ai.ats.scorer import ATSScorer
from app.ai.ats.recommendation_engine import RecommendationEngine
from app.models.ats_result import ATSResult
from app.models.application import Application

class AIEvaluationService:

    @staticmethod
    def evaluate(
        db: Session,
        candidate_id: int,
        job_id: int,
        application_id: int,
    ):

        # -----------------------------------
        # Fetch Resume
        # -----------------------------------

        resume = (
            db.query(ResumeData)
            .filter(
                ResumeData.candidate_id == candidate_id
            )
            .first()
        )

        if resume is None:
            raise ValueError("Resume not found.")

        # -----------------------------------
        # Fetch Job
        # -----------------------------------

        job = (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

        if job is None:
            raise ValueError("Job not found.")

        # -----------------------------------
        # Resume Skills
        # -----------------------------------

        resume_skills = []

        if resume.extracted_skills:

            if isinstance(resume.extracted_skills, str):

                resume_skills = [
                    s.strip()
                    for s in resume.extracted_skills.split(",")
                    if s.strip()
                ]

            elif isinstance(resume.extracted_skills, list):

                resume_skills = resume.extracted_skills

        # -----------------------------------
        # Job Skills
        # -----------------------------------

        job_skills = job.required_skills or []

        # -----------------------------------
        # Skill Matching
        # -----------------------------------

        matched, missing = SkillMatcher.match(
            resume_skills,
            job_skills,
        )

        # -----------------------------------
        # ATS Score
        # -----------------------------------

        score = ATSScorer.calculate(
            matched,
            missing,
        )

        # -----------------------------------
        # Recommendation
        # -----------------------------------

        recommendation = RecommendationEngine.predict(score)

        # -----------------------------------
        # Save ATS Result
        # -----------------------------------

        existing_result = (
            db.query(ATSResult)
            .filter(
                ATSResult.application_id == application_id
            )
            .first()
        )

        if existing_result:

            existing_result.ats_score = score
            existing_result.matching_skills = matched
            existing_result.missing_skills = missing
            existing_result.ai_summary = recommendation["summary"]
            existing_result.recommendation = recommendation["recommendation"]

        else:

            ats_result = ATSResult(

                application_id=application_id,

                ats_score=score,

                matching_skills=matched,

                missing_skills=missing,

                ai_summary=recommendation["summary"],

                recommendation=recommendation["recommendation"],
            )

            db.add(ats_result)

        db.commit()

        return {

            "ats_score": score,

            "matched_skills": matched,

            "missing_skills": missing,

            "recommendation": recommendation["recommendation"],

            "summary": recommendation["summary"],
        }
        return result