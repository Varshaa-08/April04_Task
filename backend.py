# backend.py (FastAPI Backend)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

data_store = []  # Temporary storage

class UserData(BaseModel):
    username: str
    age: int

@app.post("/submit/")
def submit_data(user: UserData):
    data_store.append(user)
    return {"message": "Data submitted successfully"}

@app.get("/data/", response_model=List[UserData])
def get_data():
    return data_store

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
