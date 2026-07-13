from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import CandidateRegister
from app.core.security import (
    hash_password,
    verify_password,
)
from app.core.jwt_handler import create_access_token


class CandidateAuthService:

    @staticmethod
    def register(
        db: Session,
        candidate: CandidateRegister,
    ):

        # Password confirmation
        if candidate.password != candidate.confirm_password:
            raise ValueError(
                "Passwords do not match."
            )

        # Check duplicate email
        existing_user = (
            db.query(User)
            .filter(User.email == candidate.email)
            .first()
        )

        if existing_user:
            raise ValueError(
                "Email already registered."
            )

        # Create user
        user = User(
            full_name=f"{candidate.first_name} {candidate.last_name}",
            email=candidate.email,
            password_hash=hash_password(candidate.password),
            role="Candidate",
            is_active=True,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role,
                "user_id": user.id,
            }
        )

        return {
            "access_token": token,
            "token_type": "Bearer",
            "role": user.role,
        }

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ):

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            raise ValueError(
                "Invalid email or password."
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role,
                "user_id": user.id,
            }
        )

        return {
            "access_token": token,
            "token_type": "Bearer",
            "role": user.role,
        }