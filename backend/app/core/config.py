from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    # =====================================================
    # Database
    # =====================================================

    DATABASE_URL: str

    # =====================================================
    # JWT
    # =====================================================

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # =====================================================
    # Uploads
    # =====================================================

    UPLOAD_FOLDER: str

    # =====================================================
    # OpenAI
    # =====================================================

    OPENAI_API_KEY: Optional[str] = None

    # =====================================================
    # Email (Optional until SMTP is configured)
    # =====================================================

    MAIL_FROM: Optional[str] = None

    MAIL_USERNAME: Optional[str] = None

    MAIL_PASSWORD: Optional[str] = None

    MAIL_SERVER: Optional[str] = None

    MAIL_PORT: Optional[int] = None

    MAIL_USE_TLS: bool = True

    MAIL_USE_SSL: bool = False

    MAIL_FROM_NAME: str = "Pranaga Solutions"

    # =====================================================
    # Pydantic Settings
    # =====================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()