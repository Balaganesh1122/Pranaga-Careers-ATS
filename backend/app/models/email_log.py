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
from sqlalchemy import Text

class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False,
    )

    recipient = Column(
        String(150),
        nullable=False,
    )

    subject = Column(
        String(255),
        nullable=False,
    )

    email_type = Column(
        String(100),
        nullable=False,
    )


    # Welcome
    # Application
    # Interview
    # Offer
    # Rejection

    status = Column(
        String(50),
        nullable=False,
        default="Sent",
    )
    # Sent / Failed

    error_message = Column(
        Text,
        nullable=True,
    )

    sent_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    application = relationship(
        "Application",
        back_populates="email_logs",
    )