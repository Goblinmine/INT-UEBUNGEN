import requests
from datetime import datetime as dt, timedelta
import pytz

DEBUG = False

def is_night(lat: float, lng: float) -> bool:
    parameters = {
        'lat':lat,
        'lng':lng,
        'formatted': 0
    }
    now = get_time(lat, lng)
    datetime_format = "%Y-%m-%dT%H:%M:%S%z"

    response = requests.get('https://api.sunrise-sunset.org/json', parameters)
    response.raise_for_status()

    sunset = dt.strptime(response.json()['results']['sunset'], datetime_format)
    sunrise = dt.strptime(response.json()['results']['sunrise'], datetime_format)
    sunrise_ofset = sunrise + timedelta(days=1)

    return (now > sunset) and (now < sunrise_ofset)


def get_time(lat: float, lng: float) -> dt:
    parameters = {
        'key':'R7TIXHW7ALW6',
        'format':'json',
        'by':'position',
        'lat':lat,
        'lng':lng,
    }
    result = requests.get('http://api.timezonedb.com/v2.1/get-time-zone', parameters)
    result.raise_for_status()
    
    return dt.now(tz=pytz.timezone(result.json()['zoneName']))


def iss_overhead(lat: float, lng: float) -> bool:
    iss_lat, iss_lng = get_iss_position()
    return (((iss_lat <= lat+5) and (iss_lat >= lat-5)) and ((iss_lng <= lng+5) and (iss_lng >= lng-5)))

def get_iss_position() -> tuple[float, float]:
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()

    iss_lat = float(response_iss.json()['iss_position']['latitude'])
    iss_lng = float(response_iss.json()['iss_position']['longitude'])
    
    return iss_lat, iss_lng

    
def main(lat: float, lng: float, debug_output = False) -> None:
    global DEBUG
    DEBUG = debug_output

    try:
        if not is_night(lat, lng): exit()
        print(f'ISS is{"" if iss_overhead(lat, lng) else " not"} over your head!!')
            
    except Exception as ex:
        print(f'ERROR: {ex}')

if __name__ == '__main__':
    main(lat=46.636459, lng=14.312225, debug_output=True)