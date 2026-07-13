from app.ai.ats.synonym_engine import SKILL_SYNONYMS


class SkillMatcher:

    @staticmethod
    def normalize(skills):

        if not skills:
            return set()

        normalized = set()

        for skill in skills:

            if not skill:
                continue

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

    @staticmethod
    def match(candidate_skills, job_skills):
        """
        Alias for compare().
        Keeps compatibility with older code.
        """

        return SkillMatcher.compare(
            candidate_skills,
            job_skills,
        )