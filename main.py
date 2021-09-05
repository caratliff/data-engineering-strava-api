from typing import Optional
from fastapi import FastAPI
import uvicorn
from strava_data import activities

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/")
async def getActivities():
    return {"Activities": activities}
    
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}