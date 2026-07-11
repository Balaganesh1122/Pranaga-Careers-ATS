from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy import JSON
from sqlalchemy.sql import func

from app.core.database import Base


class ATSResult(Base):
    __tablename__ = "ats_results"

    id = Column(Integer, primary_key=True, index=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False,
        unique=True,
    )

    ats_score = Column(Float)

    matching_skills = Column(JSON)

    missing_skills = Column(JSON)

    ai_summary = Column(Text)

    recommendation = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    application = relationship(
        "Application",
        back_populates="ats_result",
    )