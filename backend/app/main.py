from fastapi import FastAPI
from sqlalchemy import text

import app.models
from app.core.database import engine
from app.api.jobs import router as jobs_router
from app.api.candidates import router as candidate_router
from app.api.applications import router as application_router
from app.api.resume import router as resume_router
from app.api.recruiter import router as recruiter_router
from app.api.application_submission import (
    router as application_submission_router,
)
from app.api.auth import router as auth_router
from app.api.admin import router as admin_router
from app.api.public.jobs import router as public_jobs_router
from app.api.public.home import router as public_home_router
from app.api.public.departments import router as public_departments_router
from app.api.public.locations import router as public_locations_router
from app.api.public.employment_types import router as public_employment_types_router
from app.api.public.work_modes import router as public_work_modes_router
from app.api.public.experiences import router as public_experiences_router
from app.api.candidate_auth import router as candidate_auth_router
from app.api.candidate_profile import router as candidate_profile_router
from app.api.resume_upload import router as resume_upload_router
from app.api.job_application import router as job_application_router
from app.api.candidate_dashboard import router as candidate_dashboard_router
from app.api.recruiter_analytics import router as recruiter_analytics_router
from app.api.application_submission import router as application_submission_router




app = FastAPI(
    title="Pranaga Careers ATS API",
    description="AI Powered Career Portal & ATS System",
    version="1.0.0"
)


app.include_router(jobs_router)
app.include_router(candidate_router)
app.include_router(application_router)
app.include_router(resume_router)
app.include_router(application_submission_router)
app.include_router(auth_router)
app.include_router(recruiter_router)
app.include_router(admin_router)
app.include_router(public_jobs_router)
app.include_router(public_home_router)
app.include_router(public_departments_router)
app.include_router(public_locations_router)
app.include_router(public_employment_types_router)
app.include_router(public_work_modes_router)
app.include_router(public_experiences_router)   
app.include_router(candidate_auth_router)
app.include_router(candidate_profile_router)
app.include_router(resume_upload_router)
app.include_router(job_application_router)
app.include_router(candidate_dashboard_router)
app.include_router(recruiter_analytics_router)





@app.get("/")
def root():
    return {
        "message": "Welcome to Pranaga Careers ATS API 🚀"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/db-test")
def db_test():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"database": "Connected Successfully ✅"}
    except Exception as e:
        return {
            "database": "Connection Failed ❌",
            "error": str(e)
        }