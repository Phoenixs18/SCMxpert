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




# Create a random secret key that will be used to sign the JWT tokens.
# To generate a secure random secret key use the command: openssl rand -hex 32
# copy the output to the variable SECRET_KEY
# Create a variable ALGORITHM with the algorithm used to sign the JWT token and set it to "HS256".
# Create a variable for the expiration of the token.

SECRET_KEY='0e3c7d0cd7bfb666790876e2b576ca61c540995e8c7b51fea8301a90c90aefa7' ##generated using openssl
ALGORITHM="HS256" ##private key
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Define a Pydantic Model that will be used in the token endpoint for the response.
# Create a utility function to generate a new access token.

from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from .user import Token, TokenData, UserInDB 
from .config import authenticate_user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Update get_current_user to receive the same token as before, but this time, using JWT tokens.
# Decode the received token, verify it, and return the current user.
# If the token is invalid, return an HTTP error right away.

from typing import Annotated
from fastapi import Depends, HTTPException, status

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(user, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



# Create a timedelta with the expiration time of the token.
# Create a real JWT access token and return it


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(user, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}