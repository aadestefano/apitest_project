from fastapi import FastAPI
import random


app = FastAPI()


@app.get("/")
def root():
    return {"example": "This is an example", "data": 0}


