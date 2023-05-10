from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from mongoengine import  connect
from fastapi.middleware.cors import CORSMiddleware
from bson import json_util
from user import NewUser, User, Login, NewShipment, Shipments
import json
import re

from pymongo import MongoClient

app=FastAPI()

myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["SCMXpert"]
col1=db["user"]
col2=db["shipments"]
col3=db["Device_Data_Stream"]



# connect(db="SCMXpert", host="localhost", port=27017)
# connect(db="SCMXpert", host="mongodb+srv://shruti:1QKN3hyur0zCZCjp@cluster0.avltwbb.mongodb.net/?retryWrites=true&w=majority")


origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500", 
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)

def validation(User:NewUser):
    # assigning password variables
    password_regex="((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{3,20})"
    user_password=User.password
    compile_pass=re.compile(password_regex)
    search=re.search(compile_pass,user_password)


    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    user_email =User.email

    email_valid =re.fullmatch(email_regex, user_email)

@app.post("/register")
# def add_user(user:NewUser):
#     new_user=User(username=user.username,
#                   email=user.email,
#                   password=get_password_hash(user.password))

#     # new_user.save()
#     col1.insert_one(dict(user))
#     return{"message":"You are successfully signed in. Login using the same credentials."}

async def add_user(user: NewUser):
    new_user=col1.find_one({"username":user.username})
    validation(user)
    if new_user:
        raise HTTPException(
            status_code=400,detail="User with same username or email already exists."
        )
    else:
        hashed_pass=get_password_hash(user.password)
        user.password=hashed_pass
        col1.insert_one(dict(user))
    # this returns the user created --return (create_user)
    return {"message":"You are successfully signed in. Login using the same credentials."}


@app.post("/login")
# def authenticate_user(user:Login):
#     user1 = json.loads(User.objects.get(username=user.username).to_json())
#     if not user1:
#         return False
#     if not verify_password(user.password, user1['password']):
#      return False
    
#     access_token = create_access_token(data={"token":user1["username"]})
#     return {"access_token": access_token,"token_type": "bearer"}


async def authenticate_user(user:Login):
    user_data=col1.find_one({"username":user.username})
    if not user_data:
        raise HTTPException(
            status_code=400,detail="User not found."
        )
    if not verify_password(user.password,user_data["password"]):
        raise HTTPException(
            status_code=400, detail="Incorrect Password."
        )    
    access_token = create_access_token(data={"token":user_data["username"]})
    return{"access_token":access_token,"token_type":"bearer"}

    


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



async def get_current_user(token:str= Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception
    return payload


@app.get("/dashboard")
def validity_check(token: str = Depends(get_current_user)):
    if token:
        return {"Logged in":token}


@app.post("/shipment")
def add_shipment(shipment:NewShipment, token: Login =Depends(get_current_user)):
    if token:
        new_shipment=Shipments(invoice_no=shipment.invoice_no,
                           container_no= shipment.container_no,
                           shipment_description= shipment.shipment_description,
                           route_details= shipment.route_details,
                           goods_type=shipment.goods_type,
                           device=shipment.device,
                           expected_delivery_date=shipment.expected_delivery_date,
                           PO_number=shipment.PO_number,
                           delivery_no=shipment.delivery_no,
                           NDC_no=shipment.NDC_no,
                           batch_id=shipment.batch_id,
                           serial_no_of_goods=shipment.serial_no_of_goods)


        new_shipment.save()
        return {"message": "Shipment created successfully"}

    else:
        return {"message": "Shipment not created"}

    

@app.get('/devicedata')
def get_devicedata(token:str=Depends(get_current_user)):
    if token:
        data = col3.find({},{"_id":0})
        response = json.loads(json_util.dumps(data))
        return response
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Access'
        )





    

# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)]
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token", response_model=Token)
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
# ):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}





