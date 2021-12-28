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


@app.get("/dbPeopleDetails")
def createPeopleDetailsDB():

    return create_people_database()

@app.get("/clearPeopleDB")
def clearPeopleDatabase():

    return clear_people_database()

@app.post("/addPeopleDetails")
def addPeopleDetails(name: str = Form(...), email: str = Form(...), notes: str = Form(...)):

    return add_people_details(name, email, notes)

@app.get("/peopleDetailsFromDatabase")
def getPeopleFromDatabase():

    return get_people_from_db()

@app.post("/checkLoginDetails")
def checl_login_details(user: str = Form(...), pwd: str = Form(...)):

    username = "thePatBinDatabase"
    password = "iAmAPassword"

    if (user == username) and (pwd == password):

        return RedirectResponse("/ui/index.html", status.HTTP_302_FOUND)
    
    else:

        return RedirectResponse("/ui/bruh.html", status.HTTP_302_FOUND)


@app.get("/makeManagementTable")
def createMangementTable():

    return create_meanagement_tables()

@app.get("/clearManagementTable")
def clearManagementTable():

    return clear_management_tables()

@app.post("/addManagementTask")
def addManagementTask(task: str = Form(...)):

    return add_to_managemnent_table(task)

@app.get("/getTasksFromDB")
def getTasksFromDB():

    return get_management_tasks_from_db()