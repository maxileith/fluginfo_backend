from amadeus.client.errors import ClientError, ServerError, NotFoundError
from .errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
import re
from .utils import split_flight_number, get_flight_schedule

class FlightRoute:

    @staticmethod
    def get_advanced(carrier_code: str, number: int, date: str):
        # load availabilities
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

        data = response.result['data']

        if len(data) == 0:
            raise AmadeusNothingFound

        return {
            'departureIata': data[0]['flightPoints'][0]['iataCode'],
            'arrivalIata': data[0]['flightPoints'][-1]['iataCode'],
        }

    @staticmethod
    def get(flight_number: str, date: str) -> dict:
        carrier_code, number = split_flight_number(flight_number)
        return FlightRoute.get_advanced(carrier_code, number, date)
