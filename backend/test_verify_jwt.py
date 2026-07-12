from pprint import pprint

from app.core.jwt_handler import (
    create_access_token,
    verify_access_token,
)

token = create_access_token(
    {
        "sub": "ganesh@pranaga.com",
        "role": "Recruiter",
    }
)

print("Generated Token:\n")
print(token)

print("\nDecoded Payload:\n")

payload = verify_access_token(token)

pprint(payload)