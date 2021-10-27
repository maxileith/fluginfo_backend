from .foundation import amadeus_client
from amadeus.client.errors import ResponseError, ClientError
from .errors import AmadeusBadRequest, AmadeusNothingFound
import re


FLIGHT_NUMBER_PATTERN = r'^([A-Z0-9][A-Z0-9])([0-9][0-9][0-9][0-9]?)$'


class FlightRoute:

    def __init__(self: object, flight_number: str, date: str) -> object:
        self.__flight_number = flight_number
        self.__date = date

    def __split_flight_number(self: object, flight_number: str) -> tuple:
        result = re.match(FLIGHT_NUMBER_PATTERN, flight_number)
        try:
            carrier_code = result.group(1)
            number = result.group(2)
        except AttributeError:
            raise AmadeusBadRequest
        return carrier_code, number

    def go(self: object) -> dict:
        carrier_code, number = self.__split_flight_number(self.__flight_number)
        # load availabilities
        try:
            response = amadeus_client.schedule.flights.get(
                carrierCode=carrier_code,
                flightNumber=number,
                scheduledDepartureDate=self.__date,
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
