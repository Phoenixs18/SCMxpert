# Create a utility function to hash a password coming from the user.
# Another utility to verify if a received password matches the hash stored.
# Another one to authenticate and return a user.


from passlib.context import CryptContext ##to hash the password
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from test import get_user

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto") ##schemes="bcrypt" is hash algorithm, pass within list so that multiple algorithms can be passed
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def get_password_hash(password:str):
    return pwd_context.hash(password)

def verify_password(normal,hashed):
    return pwd_context.verify(normal, hashed)
    
def authenticate_user(user, username: str, password:str):
    user=get_user(user, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
    
