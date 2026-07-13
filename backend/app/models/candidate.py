from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    # =====================================================
    # Personal Information
    # =====================================================

    first_name = Column(String(100), nullable=False)

    middle_name = Column(String(100), nullable=True)

    last_name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(20), nullable=False)

    country = Column(String(100), nullable=True)

    state = Column(String(100), nullable=True)

    city = Column(String(100), nullable=True)

    # =====================================================
    # Professional Information
    # =====================================================

    highest_education = Column(String(150), nullable=True)

    years_of_experience = Column(Float, default=0)

    current_company = Column(String(150), nullable=True)

    current_designation = Column(String(150), nullable=True)

    expected_ctc = Column(Float, nullable=True)

    current_ctc = Column(Float, nullable=True)

    notice_period = Column(String(100), nullable=True)

    # =====================================================
    # Professional Links
    # =====================================================

    linkedin_url = Column(String(255), nullable=True)

    github_url = Column(String(255), nullable=True)

    portfolio_url = Column(String(255), nullable=True)

    # =====================================================
    # Audit
    # =====================================================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # =====================================================
    # Relationships
    # =====================================================

    applications = relationship(
        "Application",
        back_populates="candidate"
    )

    resume = relationship(
    "ResumeData",
    back_populates="candidate",
    uselist=False,
    cascade="all, delete-orphan",
)