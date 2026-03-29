from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    if len(password.encode("utf-8")) > 72:
        password = hashlib.sha512(password.encode("utf-8")).hexdigest()
    return pwd_context.hash(password)

def verify_password(plain_password, hash_password) -> bool:
    if len(plain_password.encode("utf-8")) > 72:
        plain_password = hashlib.sha512(plain_password.encode("utf-8")).hexdigest()
    return pwd_context.verify(plain_password, hash_password)