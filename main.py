from fastapi import FastAPI
import uvicorn
import json

app = FastAPI(
    title = 'Strava API',
    description='Application scrapes Strava Application API of an athlete to display up-to-date Strava activities.'
)

with open('data.json') as d:
    data = json.load(d)

@app.get('/')
async def get_athlete_activities():
    return {"activities": data}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')