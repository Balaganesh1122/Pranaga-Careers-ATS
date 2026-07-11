from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class ScreeningAnswer(Base):
    __tablename__ = "screening_answers"

    id = Column(Integer, primary_key=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False,
        unique=True,
    )

    work_authorization = Column(Boolean)

    notice_period = Column(String(50))

    internship_available = Column(Boolean)

    application = relationship(
        "Application",
        back_populates="screening_answer",
    )