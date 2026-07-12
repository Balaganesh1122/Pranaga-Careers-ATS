from app.core.security import hash_password

password = "Ganesh@123"

hashed = hash_password(password)

print(hashed)