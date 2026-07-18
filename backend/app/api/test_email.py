from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.email.email_service import EmailService

router = APIRouter()


@router.get("/test-email")
def test_email(db: Session = Depends(get_db)):

    print("Inside Test Email API")
    print("Sending email to:", "balaganeshgolla70@gmail.com")

    success = EmailService.send_template_email(
        db=db,
        application_id=1,
        to_email="balaganeshgolla70@gmail.com",
        subject="Pranaga ATS Email Test",
        template_name="application_confirmation.html",
        email_type="Test",
        context={
            "candidate_name": "Ganesh",
            "job_title": "AI Engineer",
            "company_name": "Pranaga Solutions",
        },
    )

    return {
        "success": success
    }