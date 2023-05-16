from fastapi import HTTPException
from models import User
import re


def validation(user:User):
    # assigning password variables
    user_password=user.password
    password_regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    compile_pass=re.compile(password_regex)
    search=re.search(compile_pass,user_password)

    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    user_email =user.email
    email_valid =re.fullmatch(email_regex, user_email)


    if len(user.username)==0 or len(user.email)==0:
      raise HTTPException(
        status_code=400,detail= "Username or Email is empty"
     )
    elif len(user.username)>8:
      raise HTTPException(
        status_code=400,detail= "Username should not exceed 8 characters"
     )

    if not search:
      raise HTTPException(
        status_code=400,detail= "Password must contain one uppercase, special character and number"
     )
 
    elif not email_valid:
      raise HTTPException(
        status_code=400,detail= "Invalid Email!"
     )