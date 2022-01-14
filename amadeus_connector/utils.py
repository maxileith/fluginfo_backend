import re
import math
from functools import lru_cache, wraps
from fluginfo.settings import CACHE_TIMEOUT, DEBUG
from time import monotonic_ns
from .errors import AmadeusBadRequest

DURATION_REGEX = r'^PT((\d+)H)?((\d+)M)?$'

def duration_to_minutes(src: str) -> int:
    result = re.match(DURATION_REGEX, src)

    try:
        h = int(result.group(2))
    except TypeError:
        h = 0
    
    try:
        m = int(result.group(4))
    except TypeError:
        m = 0

    return h * 60 + m


def inches_to_cm(inches: float) -> int:
    return round(inches * 2.54)

cache_timeout = 0 if DEBUG else CACHE_TIMEOUT

# https://blog.soumendrak.com/cache-heavy-computation-functions-with-a-timeout-value
def timed_lru_cache(
    _func=None, *, seconds: int = cache_timeout, maxsize: int = 128, typed: bool = False
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
            if monotonic_ns() >= f.expiration:
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
    result = re.match(
        r'^([A-Z0-9][A-Z0-9])([0-9][0-9][0-9][0-9]?)$', flight_number)
    try:
        carrier_code = result.group(1)
        number = result.group(2)
    except AttributeError:
        raise AmadeusBadRequest
    return carrier_code, number
