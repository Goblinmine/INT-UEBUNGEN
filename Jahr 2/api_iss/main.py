import requests
from datetime import datetime as dt, timedelta

DEBUG = False

def is_night(pos: tuple[float, float]) -> bool:
    
    # We don't need to worry about time zones and daylight saving time
    # because the Sunrise API provides its responses in UTC time without any offsets
    parameters = {
        'lng':pos[0],
        'lat':pos[1],
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

# split in iss_overhead and get_iss_position for easier use in part II

def iss_overhead(pos: tuple[float, float]) -> bool:
    iss_pos = get_iss_position()
    return (((iss_pos[1] <= pos[1]+5) and (iss_pos[1] >= pos[1]-5)) and ((iss_pos[0] <= pos[0]+5) and (iss_pos[0] >= pos[0]-5)))

def get_iss_position() -> tuple[float, float]:
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()

    iss_lat = float(response_iss.json()['iss_position']['latitude'])
    iss_lng = float(response_iss.json()['iss_position']['longitude'])
    
    if DEBUG: print(f'DEBUG: ISS pos -> lat: {iss_lat}, lng: {iss_lng}')
    
    return iss_lng, iss_lat 

    
def main(pos: tuple[float, float], debug_output = False) -> None:
    global DEBUG
    DEBUG = debug_output

    try:
        if not is_night(pos):
            print('You are not gonna see the ISS because its day!')
            return
        print(f'ISS is{"" if iss_overhead(pos) else " not"} over your head!!')
            
    except Exception as ex:
        print(f'ERROR: {ex}')

if __name__ == '__main__':
    main(pos=(14.312225, 46.636459))