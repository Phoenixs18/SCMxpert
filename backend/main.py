# ## Part 1 - import CORS
# ## allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources


# from fastapi import FastAPI, HTTPException, Depends, status
# from fastapi.middleware.cors import CORSMiddleware


# app=FastAPI() 


# ## CORS - Cross Origin Resource Sharing , default = disabled
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], ## * - allow all origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# ## Part 2- post user details with hash password

# from .user import NewUser, User


# @app.post("/add_user")
# def add_user(user:NewUser):
#     NewUser=User(username=user.username,
#                   email=user.email,
#                   password=get_password_hash(user.password ))
    
#     NewUser.save()
#     return("Successfully signed in. Login using same credentials")


