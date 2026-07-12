from app.core.jwt_handler import create_access_token

from app.core.jwt_handler import verify_access_token

token = create_access_token(
    {
        "sub": "ganesh@test.com",
        "role": "Admin",
    }
)

print(token)

payload = verify_access_token(token)

print(payload)