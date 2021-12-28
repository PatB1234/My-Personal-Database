import sqlite3 as driver
from sqlite3.dbapi2 import Cursor
from pydantic import BaseModel
from typing import Optional
import os, jwt
from passlib.context import CryptContext

DATABASE_URL = 'db/database.db'

def create_email_password_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS EMAIL_PASSWORD (EMAIL TEXT, PASSWORD TEXT, TYPE TEXT)")

def clear_email_password_table():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("DELETE FROM EMAIL_PASSWORD;")
    database.commit()

def add_email_password(email: str, password: str, type: str):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"INSERT INTO EMAIL_PASSWORD (Email, Password, Type)  VALUES ('{email}', '{password}', '{type}'); ")
    database.commit()

def get_email_pwd():

    with driver.connect(DATABASE_URL) as mdb:

        return [
            dict(item = m[0], status = m[1], pie = m[2])
            for m in mdb.execute(
                f"SELECT * FROM EMAIL_PASSWORD;"
            ).fetchall()
        ]

def create_people_database():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS PEOPLE (NAME TEXT, EMAIL TEXT, NOTES TEXT)")

def clear_people_database():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("DELETE FROM PEOPLE;")
    database.commit()

def add_people_details(name: str, email: str, notes: str):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"INSERT INTO PEOPLE (Name, Email, Notes)  VALUES ('{name}', '{email}', '{notes}'); ")
    database.commit()

def get_people_from_db():

    with driver.connect(DATABASE_URL) as mdb:

        return [
            dict(name = m[0], email = m[1], notes = m[2])
            for m in mdb.execute(
                f"SELECT * FROM PEOPLE;"
            ).fetchall()
        ]

        
def create_meanagement_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS MANAGEMENT (TASK TEXT)")

def clear_management_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("DELETE FROM MANAGEMENT;")
    database.commit()

def add_to_managemnent_table(task):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute(f"INSERT INTO MANAGEMENT (Task) VALUES ('{task}'); ")
    database.commit()

def get_management_tasks_from_db():

    with driver.connect(DATABASE_URL) as mdb:

        return [
            dict(task = m[0])
            for m in mdb.execute(
                f"SELECT * FROM MANAGEMENT;"
            ).fetchall()
        ]