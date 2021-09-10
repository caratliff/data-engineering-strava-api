from fastapi import FastAPI
import uvicorn
import json

app = FastAPI(
    title = 'Strava API',
    description='Application scrapes Strava Application API of an athlete to display up-to-date Strava activities.'
)

with open('data.json') as d:
    data = json.load(d)

@app.get("/")
async def root():
    return {"greeting": "Welcome to my strava data collector, enter a client to obtain athelete's activities."}

@app.get('/get_activities/{client_id}')
async def get_activities():
    return {"activities": data}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
