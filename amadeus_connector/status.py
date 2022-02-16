from amadeus.client.errors import ServerError, NotFoundError, ClientError
from .errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from .utils import timed_lru_cache, get_flight_schedule, split_flight_number, duration_to_minutes
from .offers import OfferSeatmap
from .airports import Airport
from .flightroute import FlightRoute
from .foundation import bookshelf, amadeus_client, SEATMAP_OFFER_BLUEPRINT, offer_cache


class StatusExact:
    """
    This class contains methods intended for requesting the status of a flight.
    """

    @staticmethod
    def get(flight_number: str, date: str) -> dict:
        """
        Get the status of a specific flight.

        Args:
            flight_number (str): Flight number, e.g. LH439.
            date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: The given flight could not be found.

        Returns:
            dict: Status of the given flight.
        """

        # get the route of the flight
        route = FlightRoute.get(flight_number, date)

        # request the status of flights that are taking
        # the given route on the given date
        statuses = StatusSearch.get(
            departure_iata=route['departureIata'],
            arrival_iata=route['arrivalIata'],
            date=date,
        )

        # filter for right flight number
        statuses = [
            a for a in statuses if a['flightNumber'] == flight_number]

        # if there is no matching flight raise
        # AmadeusNothingFound
        if len(statuses) == 0:
            raise AmadeusNothingFound

        # keep the format, just add airport information
        statuses[0]['departure']['airport'] = Airport.details(
            statuses[0]['departure']['airport']['iata'])
        statuses[0]['arrival']['airport'] = Airport.details(
            statuses[0]['arrival']['airport']['iata'])

        # return the status
        return statuses[0]


class StatusSearch:
    """
    This class contains methods intended for search for statuses of flights.
    """

    @staticmethod
    @timed_lru_cache
    def get(departure_iata: str, arrival_iata: str, date: str) -> list:
        """
        Get status for flights traveling the given route on the given date.

        Args:
            departure_iata (str): IATA code of the departure airport, e.g. FRA.
            arrival_iata (str): IATA code of the arrival airport, e.g. DFW.
            date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: There are statuses for flights on the given route / date.

        Returns:
            list: List of statuses.
        """

        # load status by route and date
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
        # return an Amadeus Connector error if there is an error
        except ServerError as e:
            raise AmadeusServerError from e
        except ClientError as e:
            raise AmadeusBadRequest from e
        except NotFoundError as e:
            raise AmadeusNothingFound from e

        # extract the dictionaries of the response and save
        # them to the bookshelf
        dictionaries = response.result['dictionaries']
        bookshelf.add(**dictionaries)

        # extract statuses from the response
        statuses = response.result['data']

        # simplify the statuses and return
        return StatusSearch.__simplify_statuses(statuses)

    @staticmethod
    def __simplify_statuses(statuses: list) -> list:
        """
        Transform the statuses to the specified format.

        Args:
            statuses (list): List of statuses.

        Returns:
            list: Simplified list of statuses.
        """

        # create a new list to return
        simplified_statuses = list()

        # iterate over all statuses
        for s in statuses:
            # go for only non-stop
            if len(s['segments']) != 1:
                continue

            # extract the only segment
            the_only_segment = s['segments'][0]
            flight_number = the_only_segment['carrierCode'] + \
                the_only_segment['number']

            # it is possible that the aircraft name is not in the bookshelf
            # because the aircraft names are not part of the dictionaries on
            # availability searches
            try:
                # try to get the aircrafts name from the bookshelf
                aircraft = bookshelf.get(
                    'aircraft', the_only_segment['aircraft']['code'])
            except AmadeusNothingFound:
                # fallback to the code of the aircraft
                aircraft = the_only_segment['aircraft']['code']

            # write all information down into the desired format and
            # add the status to the output list
            simplified_statuses.append({
                'flightNumber': flight_number,
                'carrierCode': the_only_segment['carrierCode'],
                'departure': {
                    'airport': {
                        'iata': the_only_segment['departure']['iataCode'],
                    },
                    'at': the_only_segment['departure']['at'],
                },
                'arrival': {
                    'airport': {
                        'iata': the_only_segment['arrival']['iataCode'],
                    },
                    'at': the_only_segment['arrival']['at'],
                },
                'duration': duration_to_minutes(s['duration']),
                'aircraft': aircraft,
                'availableSeats': [
                    {
                        'classId': c['class'],
                        'seats': c['numberOfBookableSeats'],
                    } for c in the_only_segment['availabilityClasses']
                ],
            })

            # it is possible that the carrier name is not in the bookshelf
            # because the carrier names are not part of the dictionaries on
            # availability searches
            try:
                # try to get the name of the carrier from the bookshelf
                simplified_statuses[-1]['carrier'] = bookshelf.get(
                    "carriers", the_only_segment['carrierCode'])
            except AmadeusNothingFound:
                # skip if nothing is available
                pass

        # return the simplified statuses
        return simplified_statuses


class StatusSeatmap:
    """
    This class contains methods intended for requesting seatmaps for status requests.
    """

    @staticmethod
    def get(flight_number: str, date: str, travel_class: str) -> dict:
        """
        Get the seatmap of a specific flight given by the travel class and date of travel.

        Args:
            flight_number (str): Flight number, e.g. LH439.
            date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.
            travel_class (str): Travel class, e.g. Y.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: There is no seatmap for the given flight.

        Returns:
            dict: Seatmap.
        """

        # split flight number into carrier code and number
        carrier_code, number = split_flight_number(flight_number)

        # determine the route
        route = FlightRoute.get_advanced(carrier_code, number, date)

        # compose a new pseudo offer from a blueprint
        offer = StatusSeatmap.__get_offer_from_blueprint(
            departure_iata=route['departureIata'],
            arrival_iata=route['arrivalIata'],
            carrier_code=carrier_code,
            number=number,
            travel_class=travel_class,
            date=date,
        )

        # add the newly created offer to the offer cache
        hash_val = offer_cache.add([offer])[0]

        # now get and return the seatmap by utilizing the
        # existing offer seatmap method. just use hash of the
        # newly created offer and segment id 1.
        return OfferSeatmap.get(hash_val, '1')

    @staticmethod
    def __get_offer_from_blueprint(departure_iata: str, arrival_iata: str, carrier_code: str, number: str, travel_class: str, date: str) -> dict:
        """
        Create a pseudo offer from a blueprint to request seatmaps for offers that aren't existing.

        Args:
            departure_iata (str): IATA code of the departure airport, e.g. FRA.
            arrival_iata (str): IATA code of the arrival airport, e.g. DFW.
            carrier_code (str): IATA code of the carrier, e.g. LH.
            number (str): Number of the flight, e.g. 439.
            travel_class (str): Travel class, e.g. Y.
            date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.

        Returns:
            dict: Offer from blueprint.
        """

        # copy the blueprint
        offer = SEATMAP_OFFER_BLUEPRINT.copy()

        # replace everything relevant with the new
        # values
        offer['itineraries'][0]['segments'][0]['departure']['iataCode'] = departure_iata
        offer['itineraries'][0]['segments'][0]['departure']['at'] = f'{date}T00:00:00'
        offer['itineraries'][0]['segments'][0]['arrival']['iataCode'] = arrival_iata
        offer['itineraries'][0]['segments'][0]['carrierCode'] = carrier_code
        offer['itineraries'][0]['segments'][0]['number'] = number
        offer['travelerPricings'][0]['fareDetailsBySegment'][0]['class'] = travel_class

        # return the new offer
        return offer


class StatusTimings:
    """
    This class contains methods intended for requesting current timings of flights.
    """

    @staticmethod
    def get(flight_number: str, date: str) -> dict:
        """
        Returns the current timings of a flight.

        Args:
            flight_number (str): Flight number, e.g. LH439.
            date (str): Date in ISO 8601 YYYY-MM-DD format, e.g. 2022-03-01.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: There are no timings for the given flight.

        Returns:
            dict: Timings.
        """

        carrier_code, number = split_flight_number(flight_number)

        # load the flight schedule
        try:
            response = get_flight_schedule(
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

        # extract the timings from the flight schedule
        # and return
        return StatusTimings.__simplify_timings(response.result['data'][0])

    @staticmethod
    def __simplify_timings(status: dict) -> dict:
        """
        Extract timings from flight schedule.

        Args:
            status (dict): Flight schedule.

        Returns:
            dict: Timings
        """

        return {
            'departure': status['flightPoints'][0]['departure']['timings'][0]['value'][:-6],
            'arrival': status['flightPoints'][-1]['arrival']['timings'][-1]['value'][:-6],
        }
