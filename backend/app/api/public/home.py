from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.public import CareersHomeResponse
from app.services.public.home_service import HomeService

router = APIRouter(
    prefix="/api/v1/public",
    tags=["Public Careers"],
)


@router.get(
    "/home",
    response_model=CareersHomeResponse,
)
def get_home(
    db: Session = Depends(get_db),
):
    return HomeService.get_home_data(db)