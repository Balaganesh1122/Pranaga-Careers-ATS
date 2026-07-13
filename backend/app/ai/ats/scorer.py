from app.ai.ats.skill_matcher import SkillMatcher
from app.ai.ats.recommendation_engine import RecommendationEngine


class ATSScorer:

    @staticmethod
    def calculate(matched_skills, missing_skills):

        total = len(matched_skills) + len(missing_skills)

        if total == 0:
            return 0

        score = round((len(matched_skills) / total) * 100)

        return score