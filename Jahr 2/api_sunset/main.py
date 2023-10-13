import requests
from datetime import datetime as dt

parameters = {
    'lat':46.636459,
    'lng':14.312225,
    'formatted': 0
}

datetime_format = "%Y-%m-%dT%H:%M:%S%z"
time_format = "%H:%M"

response = requests.get('https://api.sunrise-sunset.org/json', parameters)
response.raise_for_status()

sunset = dt.strptime(response.json()['results']['sunset'], datetime_format).replace(tzinfo=None)
sunrise = dt.strptime(response.json()['results']['sunrise'], datetime_format).replace(tzinfo=None)

now = dt.now()

print(f'Now: {now.strftime(time_format)}, Sunrise: {sunrise.strftime(time_format)}, Sunset: {sunset.strftime(time_format)}')
if (now > sunrise) and (now < sunset):
    print('Tag')
else: print('Nacht')