from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.public.work_mode_service import WorkModeService

router = APIRouter(
    prefix="/api/v1/public",
    tags=["Public Careers"],
)


@router.get("/work-modes")
def get_work_modes(
    db: Session = Depends(get_db),
):
    return WorkModeService.get_work_modes(db)