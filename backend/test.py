
# from typing import Annotated
# from fastapi import Depends, FastAPI, HTTPException, status
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from bson import json_util
# from user import NewUser, User, Login, NewShipment, Shipments, Token, TokenData
# import json
# import re
# from validation import validation

# from db import col1,col2,col3
# from jwt import create_access_token, get_current_user
# from config import verify_password, get_password_hash, oauth2_scheme

# app=FastAPI()


# # connect(db="SCMXpert", host="localhost", port=27017)
# # connect(db="SCMXpert", host="mongodb+srv://shruti:1QKN3hyur0zCZCjp@cluster0.avltwbb.mongodb.net/?retryWrites=true&w=majority")


# origins = [
#     "http://127.0.0.1:5500",
#     "http://localhost:5500", 
#     "*"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# @app.post("/register")
# async def add_user(user: NewUser):
#     new_user=col1.find_one({"username":user.username})
#     validation(user)
#     if new_user:
#         raise HTTPException(
#             status_code=400,detail="User with same username or email already exists."
#         )
#     else:
#         hashed_pass=get_password_hash(user.password)
#         user.password=hashed_pass
#         col1.insert_one(dict(user))
#     # this returns the user created --return (create_user)
#     return {"message":"You are successfully signed in. Login using the same credentials."}


# @app.post("/login")
# async def authenticate_user(user:Login):
#     user_data=col1.find_one({"username":user.username})
#     if not user_data:
#         raise HTTPException(
#             status_code=400,detail="User not found."
#         )
#     if not verify_password(user.password,user_data["password"]):
#         raise HTTPException(
#             status_code=400, detail="Incorrect Password."
#         )    
#     access_token = create_access_token(data={"token":user_data["username"]})
#     return{"access_token":access_token,"token_type":"bearer"}

    


# @app.get("/dashboard")
# def validity_check(token: str = Depends(get_current_user)):
#     if token:
#         return {"Logged in":token}


# @app.post("/shipment")
# def add_shipment(shipment:NewShipment, token: Login =Depends(get_current_user)):
#     if token:
#         new_shipment=Shipments(invoice_no=shipment.invoice_no,
#                            container_no= shipment.container_no,
#                            shipment_description= shipment.shipment_description,
#                            route_details= shipment.route_details,
#                            goods_type=shipment.goods_type,
#                            device=shipment.device,
#                            expected_delivery_date=shipment.expected_delivery_date,
#                            PO_number=shipment.PO_number,
#                            delivery_no=shipment.delivery_no,
#                            NDC_no=shipment.NDC_no,
#                            batch_id=shipment.batch_id,
#                            serial_no_of_goods=shipment.serial_no_of_goods)


#         new_shipment.save()
#         return {"message": "Shipment created successfully"}

#     else:
#         return {"message": "Shipment not created"}

    

# @app.get('/devicedata')
# def get_devicedata(token:str=Depends(get_current_user)):
#     if token:
#         data = col3.find({},{"_id":0})
#         response = json.loads(json_util.dumps(data))
#         return response
#     else:
#         raise HTTPException(
#             status_code=401, detail='Unauthorized Access'
#         )





    

