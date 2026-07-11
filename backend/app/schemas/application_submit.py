from pydantic import BaseModel

from app.schemas.application import ApplicationCreate
from app.schemas.candidate import CandidateCreate


class ApplicationSubmissionRequest(BaseModel):
    candidate: CandidateCreate
    application: ApplicationCreate