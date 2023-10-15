# send msg if its night and the iss is in 5deg on my location

import requests
from datetime import datetime as dt, timedelta
import pytz

# parameters = {
#         'lat':46.636459,
#         'lng':14.312225,
#         'formatted': 0
#     }


def is_night(lat, lng):
    parameters = {
        'lat':lat,
        'lng':lng,
        'formatted': 0
    }
    now = get_time(lat, lng)
    # now = dt.fromtimestamp(1697230064)
    datetime_format = "%Y-%m-%dT%H:%M:%S%z"
    # time_format = "%H:%M"

    response = requests.get('https://api.sunrise-sunset.org/json', parameters)
    response.raise_for_status()

    sunset = dt.strptime(response.json()['results']['sunset'], datetime_format)
    sunrise = dt.strptime(response.json()['results']['sunrise'], datetime_format)
    sunrise_ofset = sunrise + timedelta(days=1)

    return (now > sunset) and (now < sunrise_ofset)


def get_time(lat, lng):  
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


def iss_overhead(lat, lng):
    iss_lat, iss_lng = get_iss_position()
    return (((iss_lat <= lat+5) and (iss_lat >= lat-5)) and ((iss_lng <= lng+5) and (iss_lng >= lng-5)))

def get_iss_position():
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()

    iss_lat = float(response_iss.json()['iss_position']['latitude'])
    iss_lng = float(response_iss.json()['iss_position']['longitude'])
    
    return iss_lat, iss_lng

    
def main():
    # LAT = 46.636459
    # LNG = 14.312225
    LAT = 16
    LNG = -87
   
    try:
        if not is_night(LAT, LNG):
            exit()
        
        if iss_overhead(LAT, LNG):
            print('ISS is over your head!!')
            
    except Exception as ex:
        print(f'ERROR: {ex}')

if __name__ == '__main__':
    main()