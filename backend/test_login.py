from app.core.security import verify_password
from app.models.user import User
from app.core.database import SessionLocal

db = SessionLocal()

user = db.query(User).filter(
    User.email == "ganesh@test.com"
).first()

print("Email:", user.email)
print("Hash:", user.password_hash)

result = verify_password(
    "Ganesh@123",
    user.password_hash,
)

print("Password Match:", result)