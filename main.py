from typing import Optional
from fastapi import FastAPI
import uvicorn
from strava_data import data

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
    
@app.get("/")
async def displayData():
    return{"Activities": data}