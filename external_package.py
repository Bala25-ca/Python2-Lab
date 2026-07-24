#Note: Type in Terminal to install colorama package or requests package.
#python -m pip install requests
#python -m pip install colorama

import requests

def get_weather():

    url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
    response = requests.get(url).json()
    return response['hourly']['temperature_2m']
print(get_weather())
