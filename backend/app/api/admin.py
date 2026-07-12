from fastapi import APIRouter, Depends

from app.models.user import User
from app.services.auth.dependencies import get_current_admin

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"],
)


@router.get("/dashboard")
def admin_dashboard(
    current_user: User = Depends(get_current_admin),
):
    return {
        "message": "Welcome Admin",
        "user": current_user.email,
        "role": current_user.role,
    }