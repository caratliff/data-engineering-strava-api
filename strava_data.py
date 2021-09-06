import requests
import urllib3
import pandas as pd
#from pandas import json_normalize
from decouple import config
from pandas.io.json import json_normalize

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

#allows me to keep my secrets
client_id = config('client_id', default='')
client_secret = config('client_secret', default='')
refresh_token = config('refresh_token', default='')

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']

print("Access Token obtained.")

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
data = requests.get(activites_url, headers=header, params=param).json()

activities = pd.json_normalize(data)

#Create new dataframe with desired columns
cols = ['name', 'upload_id', 'type', 'distance', 'moving_time',   
         'average_speed', 'max_speed','total_elevation_gain',
         'start_date_local'
       ]
    
activities = activities[cols]

#Separate date into start time and date
activities['start_date_local'] = pd.to_datetime(activities['start_date_local'])
activities['start_time'] = activities['start_date_local'].dt.time
activities['start_date_local'] = activities['start_date_local'].dt.date

#save output into json file
activities = activities.to_json('data.json')
