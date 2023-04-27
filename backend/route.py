# from fastapi import FastAPI
# from .user import User
# from mongoengine import connect
# import json

# app=FastAPI()

# @app.post("/add_user")
# def add_user(user:User):
#     new_user=User(username=User.username,
#                   email=User.email,
#                   password=User.password)


#     new_user.save()

#     return{"message":"You are successfully signed in. Login using the same credentials."}