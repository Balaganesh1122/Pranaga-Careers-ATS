from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Date,
    Time,
    Text,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    # =====================================================
    # Application
    # =====================================================

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False,
    )

    # =====================================================
    # Interview Details
    # =====================================================

    interview_type = Column(
        String(50),
        nullable=False,
    )
    # HR / Technical / Managerial / Final

    interview_round = Column(
        String(50),
        nullable=False,
    )
    # Round 1 / Round 2 / Final

    interviewer_name = Column(
        String(150),
        nullable=False,
    )

    interviewer_email = Column(
        String(150),
        nullable=True,
    )

    interview_date = Column(
        Date,
        nullable=False,
    )

    interview_time = Column(
        Time,
        nullable=False,
    )

    meeting_link = Column(
        String(500),
        nullable=True,
    )

    location = Column(
        String(255),
        nullable=True,
    )

    # =====================================================
    # Interview Status
    # =====================================================

    status = Column(
        String(50),
        nullable=False,
        default="Scheduled",
    )
    # Scheduled / Completed / Cancelled / Rescheduled

    # =====================================================
    # Feedback
    # =====================================================

    feedback = Column(
        Text,
        nullable=True,
    )

    rating = Column(
        Float,
        nullable=True,
    )
    # Rating out of 5

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

    application = relationship(
        "Application",
        back_populates="interviews",
    )