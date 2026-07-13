from pydantic import BaseModel
from typing import List


class ResumeUploadResponse(BaseModel):

    candidate_id: int

    file_name: str

    extracted_name: str | None

    extracted_email: str | None

    extracted_phone: str | None

    extracted_skills: List[str]

    message: str