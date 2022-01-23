from .utils import split_flight_number
from amadeus.client.errors import ServerError, NotFoundError, ClientError
from .errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from .utils import timed_lru_cache, get_flight_schedule

class StatusTimings:

    @staticmethod
    def get(flight_number: str, date:str) -> dict:

        carrier_code, number = split_flight_number(flight_number)
        
        # load status
        try:
            response = get_flight_schedule(
                carrier_code=carrier_code,
                number=number,
                date=date,
            )
        except ServerError:
            raise AmadeusServerError
        except ClientError:
            raise AmadeusBadRequest
        except NotFoundError:
            raise AmadeusNothingFound

        return StatusTimings.__simplify_timings(response.result['data'][0])

    def __simplify_timings(status: dict) -> dict:
        return {
            'departure': status['flightPoints'][0]['departure']['timings'][0]['value'][:-6],
            'arrival': status['flightPoints'][-1]['arrival']['timings'][-1]['value'][:-6],
        }