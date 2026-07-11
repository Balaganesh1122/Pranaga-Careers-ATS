from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    JSON,
    DateTime
)

from sqlalchemy.sql import func

from app.core.database import Base
from sqlalchemy.orm import relationship


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(100), nullable=False)

    department = Column(String(100), nullable=False)

    location = Column(String(100), nullable=False)

    employment_type = Column(String(50), nullable=False)

    experience = Column(String(50), nullable=False)

    education = Column(String(150), nullable=False)

    description = Column(Text, nullable=False)

    responsibilities = Column(JSON, nullable=False)

    required_skills = Column(JSON, nullable=False)

    preferred_skills = Column(JSON)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    applications = relationship(
    "Application",
    back_populates="job"
    )