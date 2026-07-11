from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume.resume_service import ResumeService

router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"],
)


@router.post(
    "/{application_id}/upload",
    response_model=ResumeResponse,
)
async def upload_resume(
    application_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return await ResumeService.upload_resume(
        db,
        application_id,
        file,
    )