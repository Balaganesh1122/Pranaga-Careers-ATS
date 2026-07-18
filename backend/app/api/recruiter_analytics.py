from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.auth.dependencies import get_current_recruiter
from app.models.user import User

from app.services.recruiter.analytics_service import AnalyticsService

from app.schemas.analytics import (
    AnalyticsOverview,
    StatusChartItem,
    ATSDistributionItem,
    JobAnalyticsItem,
    MonthlyApplicationsItem,
)

router = APIRouter(
    prefix="/api/recruiter/analytics",
    tags=["Recruiter Analytics"],
)


# ==========================================================
# Dashboard Overview
# ==========================================================

@router.get(
    "/overview",
    response_model=AnalyticsOverview,
)
def overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_recruiter),
):

    return AnalyticsService.get_overview(db)


# ==========================================================
# Status Chart
# ==========================================================

@router.get(
    "/status",
    response_model=List[StatusChartItem],
)
def status_chart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_recruiter),
):

    return AnalyticsService.get_status_chart(db)


# ==========================================================
# ATS Distribution
# ==========================================================

@router.get(
    "/ats-distribution",
    response_model=List[ATSDistributionItem],
)
def ats_distribution(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_recruiter),
):

    return AnalyticsService.get_ats_distribution(db)


# ==========================================================
# Applications Per Job
# ==========================================================

@router.get(
    "/jobs",
    response_model=List[JobAnalyticsItem],
)
def job_statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_recruiter),
):

    return AnalyticsService.get_job_statistics(db)


# ==========================================================
# Monthly Applications
# ==========================================================

@router.get(
    "/monthly",
    response_model=List[MonthlyApplicationsItem],
)
def monthly_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_recruiter),
):

    return AnalyticsService.get_monthly_applications(db)