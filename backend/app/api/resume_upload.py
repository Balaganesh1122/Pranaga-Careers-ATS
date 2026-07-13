from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.resume_upload import ResumeUploadResponse
from app.services.resume.upload_service import ResumeUploadService

router = APIRouter(
    prefix="/api/candidate",
    tags=["Resume Upload"],
)


@router.post(
    "/upload-resume/{candidate_id}",
    response_model=ResumeUploadResponse,
)
def upload_resume(
    candidate_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    return ResumeUploadService.upload_resume(
        db=db,
        candidate_id=candidate_id,
        file=file,
    )