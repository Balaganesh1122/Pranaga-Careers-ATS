from sqlalchemy import (
    Column,
    Integer,
    String,
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

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False,
    )

    interviewer_name = Column(
        String(150),
        nullable=False,
    )

    interview_type = Column(
        String(30),
        nullable=False,
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

    status = Column(
        String(30),
        default="Scheduled",
    )

    remarks = Column(
        Text,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    application = relationship(
        "Application",
        back_populates="interviews",
    )