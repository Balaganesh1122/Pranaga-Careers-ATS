from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    JSON,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    # =====================================================
    # Basic Information
    # =====================================================

    title = Column(String(150), nullable=False)

    job_code = Column(
        String(30),
        unique=True,
        nullable=False,
    )

    department = Column(String(100), nullable=False)

    team = Column(String(100), nullable=False)

    location = Column(String(100), nullable=False)

    employment_type = Column(String(50), nullable=False)

    work_mode = Column(
        String(50),
        nullable=False,
        default="Onsite",
    )

    experience = Column(String(50), nullable=False)

    education = Column(String(150), nullable=False)

    minimum_qualification = Column(
        Text,
        nullable=False,
    )

    preferred_qualification = Column(
        Text,
        nullable=True,
    )

    openings = Column(
        Integer,
        default=1,
    )

    salary_range = Column(
        String(100),
        nullable=True,
    )

    # =====================================================
    # Job Details
    # =====================================================

    about_role = Column(
        Text,
        nullable=False,
    )

    description = Column(
        Text,
        nullable=False,
    )

    responsibilities = Column(
        JSON,
        nullable=False,
    )

    required_skills = Column(
        JSON,
        nullable=False,
    )

    preferred_skills = Column(
        JSON,
        nullable=True,
    )

    nice_to_have_skills = Column(
        JSON,
        nullable=True,
    )

    benefits = Column(
        JSON,
        nullable=True,
    )

    selection_process = Column(
        JSON,
        nullable=True,
    )

    application_deadline = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    job_status = Column(
        String(30),
        nullable=False,
        default="Open",
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    posted_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
    )

    # =====================================================
    # Audit
    # =====================================================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # =====================================================
    # Relationships
    # =====================================================

    applications = relationship(
        "Application",
        back_populates="job",
    )

    recruiter = relationship(
        "User",
        foreign_keys=[posted_by],
    )