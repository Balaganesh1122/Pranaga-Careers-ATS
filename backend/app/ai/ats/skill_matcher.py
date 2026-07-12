from app.ai.ats.synonym_engine import SKILL_SYNONYMS


class SkillMatcher:

    @staticmethod
    def normalize(skills):

        normalized = set()

        for skill in skills:

            key = skill.strip().lower()

            if key in SKILL_SYNONYMS:
                normalized.add(SKILL_SYNONYMS[key])

            else:
                normalized.add(skill.strip())

        return normalized

    @staticmethod
    def compare(candidate_skills, job_skills):

        candidate = SkillMatcher.normalize(candidate_skills)

        job = SkillMatcher.normalize(job_skills)

        matched = sorted(candidate & job)

        missing = sorted(job - candidate)

        return matched, missing