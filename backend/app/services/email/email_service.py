import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.email_log import EmailLog
from app.services.email.template_loader import EmailTemplateLoader


class EmailService:

    @staticmethod
    def send_email(
        db: Session,
        application_id: int,
        to_email: str,
        subject: str,
        html_content: str,
        email_type: str,
    ) -> bool:

        if not all([
            settings.MAIL_SERVER,
            settings.MAIL_PORT,
            settings.MAIL_USERNAME,
            settings.MAIL_PASSWORD,
        ]):
            raise Exception("SMTP configuration is incomplete.")

        email_status = "Sent"
        error_message = None

        try:

            message = MIMEMultipart("alternative")

            message["Subject"] = subject
            message["From"] = (
                f"{settings.MAIL_FROM_NAME} "
                f"<{settings.MAIL_FROM}>"
            )
            message["To"] = to_email

            message.attach(
                MIMEText(html_content, "html")
            )

            if settings.MAIL_USE_SSL:

                server = smtplib.SMTP_SSL(
                    settings.MAIL_SERVER,
                    settings.MAIL_PORT,
                    timeout=30,
                )

            else:

                server = smtplib.SMTP(
                    settings.MAIL_SERVER,
                    settings.MAIL_PORT,
                    timeout=30,
                )

                if settings.MAIL_USE_TLS:
                    server.starttls()

            server.login(
                settings.MAIL_USERNAME,
                settings.MAIL_PASSWORD,
            )

            server.sendmail(
                settings.MAIL_FROM,
                to_email,
                message.as_string(),
            )

            server.quit()

        except Exception as e:

            email_status = "Failed"
            error_message = str(e)

        finally:

            log = EmailLog(
                application_id=application_id,
                recipient=to_email,
                subject=subject,
                email_type=email_type,
                status=email_status,
                error_message=error_message,
            )

            db.add(log)
            db.commit()

        return email_status == "Sent"

    @staticmethod
    def send_template_email(
        db: Session,
        application_id: int,
        to_email: str,
        subject: str,
        template_name: str,
        email_type: str,
        context: dict,
    ):

        html = EmailTemplateLoader.load_template(
            template_name,
            context,
        )

        return EmailService.send_email(
            db=db,
            application_id=application_id,
            to_email=to_email,
            subject=subject,
            html_content=html,
            email_type=email_type,
        )