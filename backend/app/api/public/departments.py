from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.public.departments_service import DepartmentService

router = APIRouter(
    prefix="/api/v1/public",
    tags=["Public Careers"],
)


@router.get("/departments")
def get_departments(
    db: Session = Depends(get_db),
):
    return DepartmentService.get_departments(db)