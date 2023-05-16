
# from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bson import json_util
import json
from models import NewUser, User, Login, NewShipment, Shipments, Token, TokenData
from validation import validation
from db import user_data,shipment_data,stream_data
from jwt import create_access_token, get_current_user
from config import verify_password, get_password_hash, oauth2_scheme

app=FastAPI()


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


@app.post("/register")
async def add_user(user: NewUser):
    new_user=user_data.find_one({"username":user.username})
    validation(user)
    if new_user:
        raise HTTPException(
            status_code=400,detail="User with same username or email already exists."
        )
    else:
        hashed_pass=get_password_hash(user.password)
        user.password=hashed_pass
        user_data.insert_one(dict(user))
    return {"message":"You are successfully signed in."}


@app.post("/login")
async def authenticate_user(user:Login):
    in_user_data=user_data.find_one({"username":user.username})
    if not in_user_data:
        raise HTTPException(
            status_code=400,detail="User not found."
        )
    if not verify_password(user.password,in_user_data["password"]):
        raise HTTPException(
            status_code=400, detail="Incorrect Password."
        )    
    access_token = create_access_token(data={"token":in_user_data["username"]})
    return{"access_token":access_token,"token_type":"bearer"}


@app.get("/dashboard")
def validity_check(token: str = Depends(get_current_user)):
    if token:
        return {"Logged in":token}


@app.post("/shipment")
def add_shipment(shipment:NewShipment, token: str =Depends(get_current_user)):
    if token:
     
        shipment_data.insert_one(dict(shipment))
        return {"message": "Shipment created successfully"}

    else:
        return {"message": "Shipment not created"}

    

@app.get('/devicedata')
def get_devicedata(token:str=Depends(get_current_user)):
    if token:
        data = stream_data.find({},{"_id":0})
        response = json.loads(json_util.dumps(data))
        return response
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Access'
        )





    

