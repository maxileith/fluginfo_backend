import amadeus
from amadeus.client.errors import ClientError, ServerError, NotFoundError
from .errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from .utils import split_flight_number, get_flight_schedule


class FlightRoute:
    """
    This class contains methods intended for requesting flight routes.
    """

    def __init__(self, amadeus_client: amadeus.Client):
        """
        Initialize flight route object.

        Args:
            self (object): Object itself.
            amadeus_client (amadeus.Client): Amadeus client instance.
        """
        self.__amadeus_client = amadeus_client

    def get_advanced(self, carrier_code: str, number: int, date: str) -> dict:
        """
        Returns the flight route of the specified flight.

        Args:
            self (object): Object itself.
            carrier_code (str): IATA code of the carrier, e.g. LH.
            number (int): Number of the flight, e.g. 439.
            date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: The given flight could not be found.

        Returns:
            dict: Flight route.

        Example return:
            {
                'departureIata': 'FRA',
                'arrivalIata': 'DFW',
            }
        """

        try:
            # load schedule
            response = get_flight_schedule(
                amadeus_client=self.__amadeus_client,
                carrier_code=carrier_code,
                number=number,
                date=date,
            )
        # return an Amadeus Connector error if there is an error
        except ServerError as e:
            raise AmadeusServerError from e
        except ClientError as e:
            raise AmadeusBadRequest from e
        except NotFoundError as e:
            raise AmadeusNothingFound from e

        # extract data from response
        data = response.result['data']

        # check if there are no schedules
        if len(data) == 0:
            # if there are no schedules raise AmadeusNothingFound
            raise AmadeusNothingFound

        # return the flight route
        return {
            'departureIata': data[0]['flightPoints'][0]['iataCode'],
            'arrivalIata': data[0]['flightPoints'][-1]['iataCode'],
        }

    def get(self, flight_number: str, date: str) -> dict:
        """
        Returns the flight route of the specified flight.

        Args:
            self (object): Object itself.
            flight_number (str): Flight number, e.g. LH438.
            date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: The given flight could not be found.

        Returns:
            dict: Flight route.

        Example return:
            {
                'departureIata': 'FRA',
                'arrivalIata': 'DFW',
            }
        """

        # split flight number into carrier and number
        carrier_code, number = split_flight_number(flight_number)

        # utilize the already existing function
        return self.get_advanced(carrier_code, number, date)
