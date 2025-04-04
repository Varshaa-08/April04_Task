from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
user_data = []

class User(BaseModel):
    username: str
    age: int

@app.post("/submit/")
async def submit_data(user: User):
    user_data.append(user.dict())
    return {"message": "Data submitted successfully"}

@app.get("/data/")
async def get_data():
    return {"data": user_data}  # Ensure it always returns a dictionary


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
