from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.public.locations_service import LocationService

router = APIRouter(
    prefix="/api/v1/public",
    tags=["Public Careers"],
)


@router.get("/locations")
def get_locations(
    db: Session = Depends(get_db),
):
    return LocationService.get_locations(db)