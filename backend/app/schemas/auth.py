from pydantic import BaseModel, EmailStr, Field


# ============================================================
# EXISTING ATS SCHEMAS
# ============================================================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    role: str


# ============================================================
# CANDIDATE REGISTRATION
# ============================================================

class CandidateRegister(BaseModel):
    first_name: str = Field(..., max_length=100)
    middle_name: str | None = None
    last_name: str = Field(..., max_length=100)
    email: EmailStr
    phone: str
    password: str = Field(..., min_length=8)
    confirm_password: str = Field(..., min_length=8)


# ============================================================
# CANDIDATE LOGIN
# ============================================================

class CandidateLogin(BaseModel):
    email: EmailStr
    password: str


# ============================================================
# COMMON AUTH RESPONSE
# ============================================================

class AuthResponse(BaseModel):
    access_token: str
    token_type: str
    role: str