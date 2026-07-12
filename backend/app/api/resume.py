from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.resume import ResumeResponse
from app.services.resume.resume_service import ResumeService

from fastapi.responses import FileResponse

from app.models.resume_data import ResumeData

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
@router.get("/download/{resume_id}")
def download_resume(
    resume_id: int,
    db: Session = Depends(get_db),
):

    resume = (
        db.query(ResumeData)
        .filter(
            ResumeData.id == resume_id
        )
        .first()
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found."
        )

    return FileResponse(
        path=resume.file_path,
        filename=resume.file_name,
        media_type=resume.mime_type,
    )