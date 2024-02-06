import requests

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "api_key"

weather_params = {
    "lat": 29.424122,
    "lon": -98.493629,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json)

