from fastapi import FastAPI
from sqlalchemy import text

import app.models
from app.core.database import engine
from app.api.jobs import router as jobs_router
from app.api.candidates import router as candidate_router
from app.api.applications import router as application_router
from app.api.resume import router as resume_router
from app.api.application_submission import (
    router as application_submission_router,
)

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