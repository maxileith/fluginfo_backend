from .foundation import amadeus_client
from .utils import split_flight_number
from amadeus.client.errors import ResponseError, ClientError
from .errors import AmadeusBadRequest, AmadeusNothingFound
from .utils import timed_lru_cache

class StatusTimings:

    @staticmethod
    @timed_lru_cache
    def get(flight_number: str, date:str) -> dict:

        carrier_code, number = split_flight_number(flight_number)
        
        # load status
        try:
            response = amadeus_client.schedule.flights.get(
                carrierCode=carrier_code,
                flightNumber=number,
                scheduledDepartureDate=date,
            )
        except ResponseError:
            raise AmadeusBadRequest
        except ClientError:
            raise AmadeusBadRequest

        for x in response.result['data']:
            if x['flightDesignator']['carrierCode'] == carrier_code and str(x['flightDesignator']['flightNumber']) == number:
                return StatusTimings.__simplify_timings(x)
            
        raise AmadeusNothingFound

    def __simplify_timings(status: dict) -> dict:
        return {
            'departure': status['flightPoints'][0]['departure']['timings'][0]['value'],
            'arrival': status['flightPoints'][-1]['arrival']['timings'][-1]['value'],
        }