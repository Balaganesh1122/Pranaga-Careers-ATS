import re

from app.ai.ats.skills_database import TECH_SKILLS


class ResumeInformationExtractor:

    @staticmethod
    def extract(text: str):

        result = {}

        # --------------------
        # Name
        # --------------------

        lines = text.split("\n")

        result["name"] = lines[0].strip()

        # --------------------
        # Email
        # --------------------

        email = re.search(
            r'[\w\.-]+@[\w\.-]+\.\w+',
            text
        )

        result["email"] = email.group(0) if email else None

        # --------------------
        # Phone
        # --------------------

        phone = re.search(
            r'(\+91[- ]?)?\d{10}',
            text
        )

        result["phone"] = phone.group(0) if phone else None

        # --------------------
        # Skills
        # --------------------

        skills_found = []

        lower_text = text.lower()

        for skill in TECH_SKILLS:

            if skill.lower() in lower_text:
                skills_found.append(skill)

        result["skills"] = sorted(list(set(skills_found)))

        return result