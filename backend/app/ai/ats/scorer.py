from app.ai.ats.skill_matcher import SkillMatcher
from app.ai.ats.recommendation_engine import RecommendationEngine


class ATSScorer:

    @staticmethod
    def calculate(candidate_skills, job_skills):

        matched, missing = SkillMatcher.compare(
            candidate_skills,
            job_skills,
        )

        total = len(job_skills)

        score = (
            round((len(matched) / total) * 100)
            if total
            else 0
        )

        recommendation = RecommendationEngine.generate(score)

        return {
            "ats_score": score,
            "matched_skills": matched,
            "missing_skills": missing,
            "recommendation": recommendation["recommendation"],
            "summary": recommendation["summary"],
        }