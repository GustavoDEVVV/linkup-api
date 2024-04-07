from passlib.context import CryptContext  # type: ignore
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = '62cb19571d5aba89bbcc372c56c336805870b1d649677f631fcb3b4ed89f5524'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
