from typing import Annotated, Any
from .controller import student_controller
from motor.core import AgnosticDatabase

from controller import student_controller
from pydantic import BeforeValidator
from fastapi import FastAPI
from motor import motor_asyncio

from src.fast_api_learning.config.config import MONGO_URI, MONGO_DB
mongodb_uri = MONGO_URI

PyObjectId = Annotated[str, BeforeValidator(str)]

client = motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.get_database(MONGO_DB) 
student_collection = db.get_collection("students")


app = FastAPI()
app.include_router(student_controller.router)

@app.get("/")
def root():
    return {"message": "Hello world"}

