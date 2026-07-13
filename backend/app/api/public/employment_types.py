from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.public.employment_type_service import EmploymentTypeService

router = APIRouter(
    prefix="/api/v1/public",
    tags=["Public Careers"],
)


@router.get("/employment-types")
def get_employment_types(
    db: Session = Depends(get_db),
):
    return EmploymentTypeService.get_employment_types(db)