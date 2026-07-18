from pydantic import BaseModel
from typing import List


# ==========================================================
# Dashboard Overview
# ==========================================================

class AnalyticsOverview(BaseModel):
    total_jobs: int
    active_jobs: int
    total_applications: int
    average_ats_score: float

    applied: int
    under_review: int
    shortlisted: int
    interview: int
    rejected: int
    offered: int
    hired: int


# ==========================================================
# Status Chart
# ==========================================================

class StatusChartItem(BaseModel):
    status: str
    count: int


# ==========================================================
# ATS Distribution
# ==========================================================

class ATSDistributionItem(BaseModel):
    range: str
    count: int


# ==========================================================
# Applications Per Job
# ==========================================================

class JobAnalyticsItem(BaseModel):
    job_title: str
    applications: int


# ==========================================================
# Monthly Applications
# ==========================================================

class MonthlyApplicationsItem(BaseModel):
    month: str
    applications: int