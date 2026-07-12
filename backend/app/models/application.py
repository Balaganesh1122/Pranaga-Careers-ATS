from enum import Enum

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class ApplicationStatus(str, Enum):
    APPLIED = "Applied"
    UNDER_REVIEW = "Under Review"
    SHORTLISTED = "Shortlisted"
    INTERVIEW = "Interview"
    REJECTED = "Rejected"
    HIRED = "Hired"


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    job_id = Column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False,
    )

    status = Column(
        String(30),
        default=ApplicationStatus.APPLIED.value,
        nullable=False,
    )

    work_authorization = Column(Boolean, nullable=False)

    notice_period = Column(String(50), nullable=True)

    internship_available = Column(Boolean, nullable=True)

    privacy_consent = Column(Boolean, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    candidate = relationship(
    "Candidate",
    back_populates="applications"
    )

    job = relationship(
    "Job",
    back_populates="applications"
    )

    resume = relationship(
    "ResumeData",
    back_populates="application",
    uselist=False,
    )

    ats_result = relationship(
    "ATSResult",
    back_populates="application",
    uselist=False,
    )

    screening_answer = relationship(
    "ScreeningAnswer",
    back_populates="application",
    uselist=False,
    )
    notes = relationship(
    "RecruiterNote",
    back_populates="application",
    cascade="all, delete-orphan",
)
    interviews = relationship(
    "Interview",
    back_populates="application",
    cascade="all, delete-orphan",
)