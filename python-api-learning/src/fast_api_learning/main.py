from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from src.fast_api_learning.config.config import MONGO_URI

mongodb_uri = MONGO_URI


def create_mongodb_client() -> MongoClient:
    client = MongoClient(mongodb_uri, server_api=ServerApi("1"))

    try:
        client.admin.command("ping")
        print("Database connection successfully established")

    except Exception as e:
        print(e)

    return client


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}
