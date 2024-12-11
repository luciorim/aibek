# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, aibek!"}


@app.get("/health")
def health_check():
    return {"status": "OK"}
