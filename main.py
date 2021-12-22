from db import *
from fastapi import FastAPI
from fastapi import status, Form
from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pydantic.errors import FrozenSetError
from starlette.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from db import *

app = FastAPI()
app.mount("/ui", StaticFiles(directory = "ui"), name = "ui")
oath2_scheme = OAuth2PasswordBearer(tokenUrl = "/token")

@app.get("/clearEmailPwd")
def clear_email_pwd():

    return clear_email_password_table()

@app.get("/dbEmailPwd")
def make_db_email_pwd():

    return create_email_password_tables()

@app.post("/addEmailPwd")
def add_email_pwd(email: str = Form(...), password: str = Form(...), type: str = Form(...)):

    return add_email_password(email, password, type)

@app.get("/emailPwd")
def getEmailPWD():
    
    return get_email_pwd()