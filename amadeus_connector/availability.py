from .foundation import bookshelf, amadeus_client, SEATMAP_OFFER_BLUEPRINT, offer_cache
from amadeus.client.errors import ResponseError, ClientError
from .errors import AmadeusBadRequest, AmadeusNothingFound
from .flightroute import FlightRoute
from .utils import timed_lru_cache, split_flight_number, split_duration
from .offers import OfferSearch, OfferDetails, OfferSeatmap
from .airports import Airport


class AvailabilityExact:

    @staticmethod
    def get(flight_number: str, date: str) -> dict:
        route = FlightRoute.get(flight_number, date)
        availabilities = AvailabilitySearch.get(
            departure_iata=route['departureIata'],
            arrival_iata=route['arrivalIata'],
            date=date,
        )
        # filter for right flight number
        availabilities = [a for a in availabilities if a['flightNumber'] == flight_number]
        try:
            return availabilities[0]
        except IndexError:
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

        return AvailabilitySearch.__simplify_availabilities(availabilities)

    @staticmethod
    def __simplify_availabilities(availabilities: list) -> list:
        simplified_availabilities = list()
        for a in availabilities:
            # go for only non-stop
            if len(a['segments']) != 1:
                continue
            # extract the only segment
            the_only_segment = a['segments'][0]
            flight_number = the_only_segment['carrierCode'] + \
                the_only_segment['number']

            # it is possible that the aircraft name is not in the bookshelf
            # because the aircraft names are not part of the dictionaries on
            # availability searches
            try:
                aircraft = bookshelf.get('aircraft', the_only_segment['aircraft']['code'])
            except AmadeusNothingFound:
                aircraft = the_only_segment['aircraft']['code']

            simplified_availabilities.append({
                'flightNumber': flight_number,
                'carrierCode': the_only_segment['carrierCode'],
                'departure': {
                    'airport': Airport.details(the_only_segment['departure']['iataCode']),
                    'at': the_only_segment['departure']['at'],
                },
                'arrival': {
                    'airport': Airport.details(the_only_segment['arrival']['iataCode']),
                    'at': the_only_segment['arrival']['at'],
                },
                'duration': split_duration(a['duration']),
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
                simplified_availabilities[-1]['carrier'] = bookshelf.get("carriers", the_only_segment['carrierCode'])
            except AmadeusNothingFound:
                pass

        return simplified_availabilities


class AvailabilitySeatmap:

    @staticmethod
    def get(flight_number: str, date: str, travel_class: str) -> dict:
        carrier_code, number = split_flight_number(flight_number)
        route = FlightRoute.get_advanced(carrier_code, number, date)
        offer = AvailabilitySeatmap.__get_offer_from_blueprint(
            departureIata=route['departureIata'],
            arrivalIata=route['arrivalIata'],
            carrier_code=carrier_code,
            number=number,
            travel_class=travel_class,
            date=date,
        )
        hash_val = offer_cache.add([offer])[0]
        return OfferSeatmap.get(hash_val, '1')

    @staticmethod
    def __get_offer_from_blueprint(departureIata: str, arrivalIata: str, carrier_code: str, number: str, travel_class: str, date: str):
        offer = SEATMAP_OFFER_BLUEPRINT.copy()
        offer['itineraries'][0]['segments'][0]['departure']['iataCode'] = departureIata
        offer['itineraries'][0]['segments'][0]['departure']['at'] = f'{date}T00:00:00'
        offer['itineraries'][0]['segments'][0]['arrival']['iataCode'] = arrivalIata
        offer['itineraries'][0]['segments'][0]['carrierCode'] = carrier_code
        offer['itineraries'][0]['segments'][0]['number'] = number
        offer['travelerPricings'][0]['fareDetailsBySegment'][0]['class'] = travel_class
        return offer
