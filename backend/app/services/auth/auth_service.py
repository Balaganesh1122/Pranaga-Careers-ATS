from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.auth import (
    LoginRequest,
    LoginResponse,
)

from app.core.security import verify_password
from app.core.jwt_handler import create_access_token


class AuthService:

    @staticmethod
    def login(
        db: Session,
        request: LoginRequest,
    ):

        user = (
            db.query(User)
            .filter(User.email == request.email)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role,
                "user_id": user.id,
            }
        )

        return LoginResponse(
            access_token=token,
            token_type="Bearer",
            role=user.role,
        )