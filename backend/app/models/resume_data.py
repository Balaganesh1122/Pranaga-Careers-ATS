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

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False,
        unique=True,
    )

    file_name = Column(String(255), nullable=False)

    file_path = Column(String(500), nullable=False)

    file_size = Column(Integer)

    mime_type = Column(String(100))

    parsed_text = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    application = relationship(
        "Application",
        back_populates="resume"
    )