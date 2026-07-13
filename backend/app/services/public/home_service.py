from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.job import Job


class HomeService:

    @staticmethod
    def get_home_data(db: Session):

        # -----------------------------
        # Departments
        # -----------------------------
        departments_query = (
            db.query(
                Job.department,
                func.count(Job.id).label("open_positions")
            )
            .filter(Job.is_active == True)
            .group_by(Job.department)
            .all()
        )

        departments = [
            {
                "name": row.department,
                "open_positions": row.open_positions,
            }
            for row in departments_query
        ]

        # -----------------------------
        # Latest Open Positions
        # -----------------------------
        featured_jobs = (
            db.query(Job)
            .filter(Job.is_active == True)
            .order_by(Job.created_at.desc())
            .limit(6)
            .all()
        )

        # -----------------------------
        # FAQs (Temporary Static Data)
        # Later we'll move this into a database table.
        # -----------------------------
        faqs = [
            {
                "question": "How long does the hiring process take?",
                "answer": "The hiring process usually takes 1–3 weeks depending on the role."
            },
            {
                "question": "Can I apply for multiple jobs?",
                "answer": "Yes. You can apply for multiple roles that match your skills."
            },
            {
                "question": "Can I update my resume after applying?",
                "answer": "Yes. You can upload a new resume from your Candidate Dashboard."
            },
            {
                "question": "Do internships convert to full-time roles?",
                "answer": "High-performing interns may receive full-time offers based on business requirements."
            }
        ]

        return {
            "hero_title": "Build Your Career with Pranaga Solutions",

            "hero_description": (
                "Work on AI, Cyber Security, Cloud, Enterprise Applications "
                "and Digital Transformation projects with our engineering teams."
            ),

            "departments": departments,

            "featured_jobs": featured_jobs,

            "faqs": faqs,
        }