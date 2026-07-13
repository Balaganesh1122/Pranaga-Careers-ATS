from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class ResumeData(Base):
    __tablename__ = "resume_data"

    id = Column(Integer, primary_key=True, index=True)

    # =====================================================
    # Candidate
    # =====================================================

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
        unique=True,
    )

    # =====================================================
    # Resume File
    # =====================================================

    file_name = Column(
        String(255),
        nullable=False,
    )

    file_path = Column(
        String(500),
        nullable=False,
    )

    file_size = Column(Integer)

    mime_type = Column(String(100))

    # =====================================================
    # Parsed Resume
    # =====================================================

    parsed_text = Column(Text)

    extracted_name = Column(String(150))

    extracted_email = Column(String(150))

    extracted_phone = Column(String(30))

    extracted_skills = Column(Text)

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
    # Relationship
    # =====================================================

    candidate = relationship(
        "Candidate",
        back_populates="resume",
    )