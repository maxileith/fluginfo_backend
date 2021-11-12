from .foundation import bookshelf, amadeus_client
from amadeus.client.errors import ResponseError, ClientError
from .errors import AmadeusBadRequest, AmadeusNothingFound
from .flightroute import FlightRoute
from .utils import timed_lru_cache


class AvailabilityExact:

    def get(flight_number: str, date: str) -> dict:
        route = FlightRoute.get(flight_number, date)
        availabilities = AvailabilitySearch.get(
            departure_iata=route['departureIata'],
            arrival_iata=route['arrivalIata'],
            date=date,
        )
        try:
            return availabilities[flight_number]
        except KeyError:
            raise AmadeusNothingFound


class AvailabilitySearch:

    @staticmethod
    @timed_lru_cache
    def get(departure_iata: str, arrival_iata: str, date: str) -> list:
        # load availabilities
        try:
            response = amadeus_client.shopping.availability.flight_availabilities.post(
                {
                    'originDestinations': [
                        {
                            'id': '1',
                            'originLocationCode': departure_iata,
                            'destinationLocationCode': arrival_iata,
                            'departureDateTime': {
                                'date': date,
                            },
                        },
                    ],
                    'travelers': [
                        {
                            'id': '1',
                            'travelerType': 'ADULT',
                        },
                    ],
                    'sources': [
                        'GDS',
                    ],
                },
            )
        except ResponseError:
            raise AmadeusBadRequest
        except ClientError:
            raise AmadeusBadRequest

        # save dictionaries
        dictionaries = response.result['dictionaries']
        bookshelf.add(**dictionaries)

        availabilities = response.result['data']

        slim_availabilities = AvailabilitySearch.__simplify_availabilities(availabilities)
        return slim_availabilities

    @staticmethod
    def __simplify_availabilities(availabilities: list) -> dict:
        simplified_availabilities = dict()
        for a in availabilities:
            # go for only non-stop
            if len(a['segments']) != 1:
                continue
            # extract the only segment
            # tos: the only segment
            the_only_segment = a['segments'][0]
            flight_number = the_only_segment['carrierCode'] + \
                the_only_segment['number']

            simplified_availabilities[flight_number] = {
                c['class']: c['numberOfBookableSeats'] for c in the_only_segment['availabilityClasses']
            }
        return simplified_availabilities


class AvailabilitySeatmap:

    @staticmethod
    def get(flight_number: str, date: str) -> dict:
        return {}
