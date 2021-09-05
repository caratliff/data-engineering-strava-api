from typing import Optional
from fastapi import FastAPI
import uvicorn
from strava_data import activities

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}