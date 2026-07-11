from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False,
    )

    recipient = Column(String(150))

    subject = Column(String(255))

    status = Column(String(50))

    sent_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    application = relationship("Application")