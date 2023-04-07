import requests

API_KEY = "de09321be213f7333ddc68f69f0e6936"
MAIL = "sue.is.developing@gmail.com"
PWD = "yjlwomkdkfetmwlx"

parameters = {
    "lat": "39.31", #52.520008",
    "lon": "-74.5", #13.404954",
    "exclude": "alerts,minutely,hourly,daily",
    "appid": API_KEY,
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
#data = response.json()
