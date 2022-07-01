import os
import requests
from twilio.rest import Client

# Open Weather API
parameters_openweather = {
    "lat": 22.572645,
    "lon": 88.363892,
    "exclude": "current,minutely,daily",
    "appid": os.environ.get("OWM_API_KEY",)
}

# Twilio API
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")


open_weather_response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params=parameters_openweather)

open_weather_response.raise_for_status()
weather_data = open_weather_response.json()
data = []
for i in range(12):
    data.append(weather_data["hourly"][i]["weather"][0]["id"])
if any(data) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Get an umbrella',
        from_=TWILIO_NUMBER,
        to='+917890377027'
    )
