import requests
from datetime import datetime as dt, timedelta
import math

DEBUG = False

def is_night(pos: tuple[float, float]) -> bool:
    """
    Determine if it is nighttime at a specific geographic location.

    This function checks if it is currently nighttime at the given longitude
    and latitude coordinates. It does so by querying the Sunrise-Sunset API
    for the sunset and sunrise times for the location and comparing them to the
    current time in UTC.

    Args:
        pos (tuple[float, float]): A tuple containing longitude and latitude.

    Returns:
        bool: True if it is nighttime; otherwise, False.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the HTTP request.

    Example:
    >>> position = (37.7749, -122.4194)  # San Francisco, CA coordinates
    >>> is_night(position)
    False  # It is not nighttime in San Francisco.
    """
    
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

def iss_overhead(pos: tuple[float, float], range = 10) -> bool:
    """
    Determine if the International Space Station (ISS) is overhead at a given location.

    This function checks whether the ISS is passing overhead a specific location on Earth
    based on its longitude and latitude. It considers the ISS as overhead
    if it is within the specified range from the given coordinates.

    Args:
        pos (tuple[float, float]): A tuple containing your longitude and latitude.
        visible_range (float): The range in which the ISS is considered overhead (default is 10 units).

    Returns:
        bool: True if the ISS is overhead; otherwise, False.

    Example:
    >>> iss_overhead((45.0, -75.0), 20.0)
    True  # ISS is overhead within a range of 20 units.
    """
    iss_pos = get_iss_position()
    distance = math.sqrt((pos[0] - iss_pos[0]) ** 2 + (pos[1] - iss_pos[1]) ** 2)
    
    return distance < range

def get_iss_position() -> tuple[float, float]:
    """
    Retrieve the current International Space Station (ISS) position.

    This function sends a request to the Open Notify API to obtain the current location
    of the ISS in terms of latitude and longitude. It then parses the response and
    returns a tuple containing the ISS's latitude and longitude.

    Returns:
        tuple[float, float]: A tuple containing the ISS's longitude and latitude.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the HTTP request.

    Example:
    >>> position = get_iss_position()
    >>> print(f'Current ISS Position: Latitude {position[1]}, Longitude {position[0]}')
    Current ISS Position: Latitude 51.6499, Longitude 0.0473
    """
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