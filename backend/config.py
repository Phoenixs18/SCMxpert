# Create a utility function to hash a password coming from the user.
# Another utility to verify if a received password matches the hash stored.
# Another one to authenticate and return a user.


from passlib.context import CryptContext ##to hash the password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
    
