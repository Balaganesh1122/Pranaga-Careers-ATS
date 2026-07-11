from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


settings = Settings()