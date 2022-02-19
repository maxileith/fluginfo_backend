import re
from time import monotonic_ns
from functools import lru_cache, wraps
from .errors import AmadeusBadRequest


def duration_to_minutes(src: str) -> int:
    """
    Parse duration string to minutes.

    Args:
        src (str): Something like "4H32M".

    Returns:
        int: The duration in minutes.
    """

    # REGEX to help extract hours and minutes
    # extract hours and minutes from string
    result = re.match(r'^PT((\d+)H)?((\d+)M)?$', src)

    try:
        # get hours
        h = int(result.group(2))
    except TypeError:
        # default to 0
        h = 0
    except AttributeError as e:
        raise AmadeusBadRequest from e

    try:
        # get minutes
        m = int(result.group(4))
    except TypeError:
        # default to 0
        m = 0
    except AttributeError as e:
        raise AmadeusBadRequest from e

    # add everything together
    return h * 60 + m


def inches_to_cm(inches: float) -> int:
    """
    Converts inches to cm.

    Args:
        inches (float): Distance in inches.

    Returns:
        int: Distance in cm.
    """

    return round(inches * 2.54)


try:
    cache_timeout
except NameError:
    cache_timeout = 0


def set_cache_timeout(seconds: int):
    """
    Set timeout of the cache in seconds.

    Args:
        seconds (int): Timout in seconds.
    """
    global cache_timeout
    cache_timeout = seconds


# https://blog.soumendrak.com/cache-heavy-computation-functions-with-a-timeout-value


def timed_lru_cache(
    _func=None, *, maxsize: int = 1024, typed: bool = False, forever: bool = False, maxseconds: int = 10e9
):
    """ Extension over existing lru_cache with timeout
    :param seconds: timeout value
    :param maxsize: maximum size of the cache
    :param typed: whether different keys for different types of cache keys
    """

    def wrapper_cache(f):
        # create a function wrapped with traditional lru_cache
        f = lru_cache(maxsize=maxsize, typed=typed)(f)
        # convert seconds to nanoseconds to set the expiry time in nanoseconds
        f.delta = (cache_timeout if maxseconds >
                   cache_timeout else maxseconds) * 10 ** 9
        f.expiration = monotonic_ns() + f.delta

        @wraps(f)  # wraps is used to access the decorated function attributes
        def wrapped_f(*args, **kwargs):
            if not forever and monotonic_ns() >= f.expiration:
                # if the current cache expired of the decorated function then
                # clear cache for that function and set a new cache value with new expiration time
                f.cache_clear()
                f.delta = (cache_timeout if maxseconds >
                           cache_timeout else maxseconds) * 10 ** 9
                f.expiration = monotonic_ns() + f.delta
            return f(*args, **kwargs)

        wrapped_f.cache_info = f.cache_info
        wrapped_f.cache_clear = f.cache_clear

        return wrapped_f

    # To allow decorator to be used without arguments
    if _func is None:
        return wrapper_cache
    else:
        return wrapper_cache(_func)


def split_flight_number(flight_number: str) -> tuple:
    """
    Split flight number to carrier code and number.

    Args:
        flight_number (str):  Flight number, e.g. LH438.

    Raises:
        AmadeusBadRequest: Client did not provide the right parameters.

    Returns:
        tuple: Carrier code, number
    """

    result = re.match(
        r'^([A-Z0-9][A-Z0-9])([0-9]+)$', flight_number)

    try:
        carrier_code = result.group(1)
        number = result.group(2)
    except AttributeError as e:
        raise AmadeusBadRequest from e

    return carrier_code, int(number)


@timed_lru_cache
def get_flight_schedule(amadeus_client: object, carrier_code: str, number: str, date: str) -> dict:
    """
    Return the flight schedule provided by amadeus unmodified.

    Args:
        amadeus_client (object): Amadeus client object.
        carrier_code (str): IATA code of the carrier, e.g. LH.
        number (int): Number of the flight, e.g. 439.
        date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.

    Returns:
        dict: Amadeus response of flight schedule.
    """

    return amadeus_client.schedule.flights.get(
        carrierCode=carrier_code,
        flightNumber=number,
        scheduledDepartureDate=date,
    )


# some key value pairs to translate aircraft cabin
# amenities to human readable strings
AIRCRAFT_CABIN_AMENITIES = {
    'aircraftCabinAmenitiesPower': {
        'PLUG': 'Plug',
        'USB_PORT': 'USB-Port',
        'ADAPTOR': 'Adaptor',
        'PLUG_OR_USB_PORT': 'Plug or USB-Port',
    },
    'aircraftCabinAmenitiesSeatTilt': {
        'FULL_FLAT': 'Full flat',
        'ANGLE_FLAT': 'Angled flat',
        'NORMAL': 'Normal',
    },
    'aircraftCabinAmenitiesWifi': {
        'FULL': 'Full',
        'PARTIAL': 'Partial',
    },
    'aircraftCabinAmenitiesEntertainment': {
        'LIVE_TV': 'Live-TV',
        'MOVIES': 'Movies',
        'AUDIO_VIDEO_ON_DEMAND': 'Audio & Video on demand',
        'TV_SHOWS': 'TV-Shows',
        'IP_TV': 'IP-TV',
    },
    'aircraftCabinAmenitiesFood': {
        'MEAL': 'Meal',
        'FRESH_MEAL': 'Fresh meal',
        'SNACK': 'Snacks',
        'FRESH_SNACK': 'Fresh snacks',
    },
    'aircraftCabinAmenitiesBeverage': {
        'ALCOHOLIC': 'Alcoholic',
        'NON_ALCOHOLIC': 'Non-Alcoholic',
        'ALCOHOLIC_AND_NON_ALCOHOLIC': 'With and without alcohol',
    },
}
