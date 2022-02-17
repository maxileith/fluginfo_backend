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
    try:
        # get minutes
        m = int(result.group(4))

    except TypeError:
        # default to 0
        m = 0

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


cache_timeout = 0

# https://blog.soumendrak.com/cache-heavy-computation-functions-with-a-timeout-value


def timed_lru_cache(
    _func=None, *, seconds: int = cache_timeout, maxsize: int = 1024, typed: bool = False, forever: bool = False
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
        f.delta = seconds * 10 ** 9
        f.expiration = monotonic_ns() + f.delta

        @wraps(f)  # wraps is used to access the decorated function attributes
        def wrapped_f(*args, **kwargs):
            if not forever and monotonic_ns() >= f.expiration:
                # if the current cache expired of the decorated function then
                # clear cache for that function and set a new cache value with new expiration time
                f.cache_clear()
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
        flight_number (str):  Flight number, e.g. LH439.

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

    return carrier_code, number


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
