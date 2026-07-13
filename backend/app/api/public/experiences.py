from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.public.experience_service import ExperienceService

router = APIRouter(
    prefix="/api/v1/public",
    tags=["Public Careers"],
)


@router.get("/experiences")
def get_experiences(
    db: Session = Depends(get_db),
):
    return ExperienceService.get_experiences(db)