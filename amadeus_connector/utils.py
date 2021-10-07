import re
import math


DURATION_REGEX = r'^PT((\d+)H)?((\d+)M)?$'

def split_duration(src: str) -> dict:
    result = re.match(DURATION_REGEX, src)

    try:
        h = int(result.group(2))
    except TypeError:
        h = 0
    
    try:
        m = int(result.group(4))
    except TypeError:
        m = 0

    return {
        'hours': h,
        'minutes': m,
    }
