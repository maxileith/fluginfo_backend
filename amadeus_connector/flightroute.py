from .foundation import amadeus_client
from amadeus.client.errors import ResponseError, ClientError
from .errors import AmadeusBadRequest, AmadeusNothingFound
import re
from .utils import timed_lru_cache


FLIGHT_NUMBER_PATTERN = r'^([A-Z0-9][A-Z0-9])([0-9][0-9][0-9][0-9]?)$'


class FlightRoute:

    @staticmethod
    def __split_flight_number(flight_number: str) -> tuple:
        result = re.match(FLIGHT_NUMBER_PATTERN, flight_number)
        try:
            carrier_code = result.group(1)
            number = result.group(2)
        except AttributeError:
            raise AmadeusBadRequest
        return carrier_code, number

    @staticmethod
    @timed_lru_cache
    def get(flight_number: str, date: str) -> dict:
        carrier_code, number = FlightRoute.__split_flight_number(flight_number)
        # load availabilities
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

        data = response.result['data']

        if len(data) == 0:
            raise AmadeusNothingFound

        return {
            'departureIata': data[0]['flightPoints'][0]['iataCode'],
            'arrivalIata': data[0]['flightPoints'][-1]['iataCode'],
        }
