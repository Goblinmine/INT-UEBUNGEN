import requests
from datetime import datetime as dt, timedelta

DEBUG = False

def is_night(lat: float, lng: float) -> bool:
    parameters = {
        'lat':lat,
        'lng':lng,
        'formatted': 0
    }
    now_utc = dt.utcnow()
    datetime_format = "%Y-%m-%dT%H:%M:%S%z"

    response = requests.get('https://api.sunrise-sunset.org/json', parameters)
    response.raise_for_status()

    sunset = dt.strptime(response.json()['results']['sunset'], datetime_format).replace(tzinfo=None)
    sunrise = dt.strptime(response.json()['results']['sunrise'], datetime_format).replace(tzinfo=None)
    sunrise_offset = sunrise + timedelta(days=1)

    # night = (now > sunset) and (now < sunrise_ofset)
    night = sunset < now_utc < sunrise_offset
    if DEBUG: print(f'DEBUG: night -> sunset: {sunset}, now_utc: {now_utc} , sunrise_offset: {sunrise_offset}, output: {night}')
    return night


def iss_overhead(lat: float, lng: float) -> bool:
    iss_lat, iss_lng = get_iss_position()
    return (((iss_lat <= lat+5) and (iss_lat >= lat-5)) and ((iss_lng <= lng+5) and (iss_lng >= lng-5)))

def get_iss_position() -> tuple[float, float]:
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()

    iss_lat = float(response_iss.json()['iss_position']['latitude'])
    iss_lng = float(response_iss.json()['iss_position']['longitude'])
    
    if DEBUG: print(f'DEBUG: ISS pos -> lat: {iss_lat}, lng: {iss_lng}')
    
    return iss_lat, iss_lng

    
def main(lat: float, lng: float, debug_output = False) -> None:
    global DEBUG
    DEBUG = debug_output

    try:
        if not is_night(lat, lng):
            print('You are not gonna see the ISS because its day!')
            return
        print(f'ISS is{"" if iss_overhead(lat, lng) else " not"} over your head!!')
            
    except Exception as ex:
        print(f'ERROR: {ex}')

if __name__ == '__main__':
    main(lat=46.636459, lng=14.312225)