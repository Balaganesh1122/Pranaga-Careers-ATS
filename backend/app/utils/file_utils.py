import os
import uuid


UPLOAD_FOLDER = "uploads"

ALLOWED_TYPES = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
]

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


def generate_filename(filename: str) -> str:
    extension = os.path.splitext(filename)[1]
    return f"{uuid.uuid4()}{extension}"