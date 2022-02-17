from copy import copy, deepcopy
from amadeus.client.errors import ServerError, NotFoundError, ClientError
from .utils import duration_to_minutes, inches_to_cm, timed_lru_cache
from .errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from .airports import Airport


class OfferSeatmap:
    """
    This class contains methods intended for requesting seatmaps for flights included in an offer.
    """

    def __init__(self: object, amadeus_client: object, bookshelf: object, offer_cache: object) -> object:
        """
        Initialize offer seatmap object.

        Args:
            self (object): Object itself.
            amadeus_client (object): Amadeus client instance.
            bookshelf (object): Bookshelf instance.
            offer_cache (object): Offer cache instance.

        Returns:
            object: Offer seatmap object.
        """
        self.__amadeus_client = amadeus_client
        self.__bookshelf = bookshelf
        self.__offer_cache = offer_cache

    @timed_lru_cache(maxseconds=60)
    def __load_seatmaps_of_offer(self: object, hash_val: str) -> list:
        """
        Loads the seatmaps of an offer from amadeus.

        Args:
            self (object): Object itself.
            hash_val (str): Hash value that identifies the offer.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: There are no seatmaps for the given offer or the offer does not exist.

        Returns:
            list: Seatmaps.
        """

        # get the offer from the cache
        # hint: this method can raise AmadeusNotFound
        # (letting the error propagate higher in the call
        # stack is intended --> don't catch)
        offer = self.__offer_cache.get([hash_val])[hash_val]

        try:
            # load seatmaps
            response = self.__amadeus_client.shopping.seatmaps.post(
                {
                    'data': [offer]
                }
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
        self.__bookshelf.add(**dictionaries)

        # return the seatmaps
        return response

    def get(self: object, hash_val: str, segment_id: int) -> dict:
        """
        Get a seatmap of a segment.

        Args:
            self (object): Object itself.
            hash_val (str): Hash value that identifies the offer.
            segment_id (int): ID of the segment of the offer.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusNothingFound: There are no seatmaps for the given offer / segment or the offer does not exist.

        Returns:
            dict: Seatmap.
        """

        # load all seatmaps of the offer
        response = self.__load_seatmaps_of_offer(hash_val)
        seatmaps = response.result['data']

        # Simplify the seatmap of the requested segment and return
        return self.__simplify_seatmap(seatmaps, segment_id)

    def __simplify_seatmap(self: object, seatmaps: list, segment_id: int) -> dict:
        """
        Selects the seatmap of the segment and transforms the seatmap into the specified format.

        Args:
            self (object): Object itself.
            seatmaps (list): List of Seatmaps.
            segment_id (int): Segment ID of the desired seatmap.

        Raises:
            AmadeusNothingFound: There is no seatmap for the given segment.

        Returns:
            dict: _description_
        """

        # filter for the seatmap for the right segment
        try:
            seatmap = list(
                filter(lambda m: m['segmentId'] == segment_id, seatmaps))[0]
        except IndexError as e:
            # raise AmadeusNothingFound if there is no
            # seatmap for the given segment
            raise AmadeusNothingFound from e

        # create the simplified seatmap dictionary
        simplified_seatmap = dict()

        # insert some metainformation such as the flightNumber
        simplified_seatmap['flightNumber'] = seatmap['carrierCode'] + \
            seatmap['number']
        simplified_seatmap['classId'] = seatmap['class']
        simplified_seatmap['departureIata'] = seatmap['departure']['iataCode']
        simplified_seatmap['arrivalIata'] = seatmap['arrival']['iataCode']
        simplified_seatmap['date'] = seatmap['departure']['at']

        # provide cabin amenities
        aircraftCabinAmenities = seatmap['aircraftCabinAmenities']

        # get information about the seat
        legSpaceUnit = aircraftCabinAmenities['seat']['spaceUnit']
        legSpaceValue = aircraftCabinAmenities['seat']['legSpace']
        legSpace = legSpaceValue if legSpaceUnit == 'CENTIMENTERS' else inches_to_cm(
            legSpaceValue)

        # make the amenities dictionary
        amenities = {
            'power': {
                'isChargeable': aircraftCabinAmenities['power']['isChargeable'],
                'type': self.__bookshelf.get('aircraftCabinAmenitiesPower', aircraftCabinAmenities['power']['powerType']),
            },
            'seat': {
                'legSpace': f'{legSpace} cm',
                'tilt': self.__bookshelf.get('aircraftCabinAmenitiesSeatTilt', aircraftCabinAmenities['seat']['tilt']),
                'images': [
                    {
                        'title': m['title'],
                        'description': m['description']['text'],
                        'href': m['href'],
                    } for m in aircraftCabinAmenities['seat']['medias'] if m['mediaType'] == 'image'
                ],
            },
            'wifi': {
                'isChargeable': aircraftCabinAmenities['wifi']['isChargeable'],
                'type': self.__bookshelf.get('aircraftCabinAmenitiesWifi', aircraftCabinAmenities['wifi']['wifiCoverage']),
            },
            'entertainment': [
                {
                    'isChargeable': e['isChargeable'],
                    'type': self.__bookshelf.get('aircraftCabinAmenitiesEntertainment', e['entertainmentType']),
                } for e in aircraftCabinAmenities['entertainment']
            ],
            'food': {
                'isChargeable': aircraftCabinAmenities['food']['isChargeable'],
                'type': self.__bookshelf.get('aircraftCabinAmenitiesFood', aircraftCabinAmenities['food']['foodType']),
            },
            'beverage': {
                'isChargeable': aircraftCabinAmenities['beverage']['isChargeable'],
                'type': self.__bookshelf.get('aircraftCabinAmenitiesBeverage', aircraftCabinAmenities['beverage']['beverageType']),
            },
        }

        # add amenities to the simplified seatmap
        simplified_seatmap['amenities'] = amenities

        simplified_seatmap['decks'] = list()

        # Compose each deck
        for deck in seatmap['decks']:

            # collect deck_infos about the deck
            deck_infos = dict()
            if 'startWingsX' in deck['deckConfiguration'].keys() and 'endWingsX' in deck['deckConfiguration'].keys():
                deck_infos = {
                    'wingsX': {
                        'start': deck['deckConfiguration']['startWingsX'],
                        'end': deck['deckConfiguration']['endWingsX'],
                    },
                    **deck_infos,
                }
            if 'exitRowsX' in deck['deckConfiguration'].keys():
                deck_infos = {
                    'exitRowsX': deck['deckConfiguration']['exitRowsX'],
                    **deck_infos,
                }

            # get to know the dimensions of the deck
            width = deck['deckConfiguration']['width']
            length = deck['deckConfiguration']['length']

            # create an empty grid for storing seat and
            # facility information
            row = [None] * width
            grid = list()
            for _ in range(0, length, 1):
                grid.append(copy(row))

            # compose seat information
            for seat in deck['seats']:
                # determine position of the seats
                try:
                    x = seat['coordinates']['x']
                    y = seat['coordinates']['y']
                except KeyError:
                    continue

                # fill the grid up with seats
                grid[x][y] = {
                    'type': 'seat',
                    'number': seat['number'],
                    'available': seat['travelerPricing'][0]['seatAvailabilityStatus'] == "AVAILABLE",
                }

                # add characteristics if available
                if 'characteristicsCodes' in seat.keys():
                    grid[x][y]['characteristics'] = [
                        self.__bookshelf.get('seatCharacteristics', c) for c in seat['characteristicsCodes']
                    ]

            # compose facility information if available
            if 'facilities' in deck.keys():
                # iterate through all facilities
                for facility in deck['facilities']:
                    # determine position of the seats
                    try:
                        x = facility['coordinates']['x']
                        y = facility['coordinates']['y']
                    except KeyError:
                        continue

                    # fill the grid up with facilities
                    grid[x][y] = {
                        'type': 'facility',
                        'name': self.__bookshelf.get('facilities', facility['code']),
                    }

            # add deck to the seatmaps
            simplified_seatmap['decks'].append({**deck_infos, 'grid': grid})

        # return the simplified seatmap
        return simplified_seatmap


class OfferDetails:
    """
    This class contains methods intended for requesting details of an offer.
    """

    def __init__(self: object, amadeus_client: object, bookshelf: object, offer_cache: object) -> object:
        """
        Initialize offer details object.

        Args:
            self (object): Object itself.
            amadeus_client (object): Amadeus client instance.
            bookshelf (object): Bookshelf instance.
            offer_cache (object): Offer cache instance.

        Returns:
            object: Offer details object.
        """
        self.__bookshelf = bookshelf
        self.__offer_cache = offer_cache
        self.__airport = Airport(
            amadeus_client=amadeus_client,
            bookshelf=bookshelf
        )

    def get(self: object, hash_val: str) -> dict:
        """
        Get details of an offer.

        Args:
            self (object): Object itself.
            hash_val (str): Hash value that identifies the offer.

        Raises:
            AmadeusNothingFound: There is no offer for the given hash value.

        Returns:
            dict: Details of the offer.
        """

        # get the offer from the cache
        # hint: this method can raise AmadeusNotFound
        # (letting the error propagate higher in the call
        # stack is intended --> don't catch)
        offer = self.__offer_cache.get([hash_val])[hash_val]

        # simplify and return the offer details
        return self.__simplify_offer(offer)

    def __simplify_offer(self: object, offer: dict) -> dict:
        """
        Take an offer and transforms it into the specified format of offer details.

        Args:
            self (object): Object itself.
            offer (dict): Original amadeus offer.

        Returns:
            dict: Offer details.
        """

        # First, get the currency
        currency = self.__bookshelf.get(
            'currencies', offer['price']['currency'])

        # create the dictionary for the specified format and
        # fill in the information.
        return {
            'price': {
                'value': float(offer["price"]["grandTotal"]),
                'currency': currency,
            },
            'itineraries': [
                {
                    'duration': duration_to_minutes(i['duration']),
                    'segments': [
                        {
                            'id': int(s['id']),
                            'departure': {
                                'airport': self.__airport.details(s['departure']['iataCode']),
                                'at': s['departure']['at'],
                            },
                            'arrival': {
                                'airport': self.__airport.details(s['arrival']['iataCode']),
                                'at': s['arrival']['at'],
                            },
                            'flightNumber': s['carrierCode'] + s['number'],
                            'carrierCode': s['carrierCode'],
                            'carrier': self.__bookshelf.get('carriers', s['carrierCode']),
                            'duration': duration_to_minutes(s['duration']),
                            'aircraft': self.__bookshelf.get('aircraft', s['aircraft']['code']),
                            'cabin': list(filter(lambda d: d['segmentId'] == s['id'], offer['travelerPricings'][0]['fareDetailsBySegment']))[0]['cabin'],
                            'classId': list(filter(lambda d: d['segmentId'] == s['id'], offer['travelerPricings'][0]['fareDetailsBySegment']))[0]['class'],
                        } for s in i['segments']
                    ],
                } for i in offer['itineraries']
            ],
        }


class OfferSearch:
    """
    This class contains methods intended for searching offers.
    """

    def __init__(self: object, amadeus_client: object, bookshelf: object, offer_cache: object) -> object:
        """
        Initialize offer search object.

        Args:
            self (object): Object itself.
            amadeus_client (object): Amadeus client instance.
            bookshelf (object): Bookshelf instance.
            offer_cache (object): Offer cache instance.

        Returns:
            object: Offer search object.
        """
        self.__amadeus_client = amadeus_client
        self.__bookshelf = bookshelf
        self.__offer_cache = offer_cache
        self.__airport = Airport(
            amadeus_client=amadeus_client,
            bookshelf=bookshelf
        )

    def __load_results(self: object, **params: dict) -> list:
        """

        Args:
            self (object): Object itself.
            **params (dict): Analog to the parameters of the following endpoint:
                             https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search/api-reference

        Raises:
            AmadeusNothingFound: There are no offers matching the parameters.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusServerError: Amadeus experienced a server error.

        Returns:
            list: Offers.
        """

        # ask the amadeus api for matching offers
        try:
            response = self.__amadeus_client.shopping.flight_offers_search.get(
                **params)
        # return an Amadeus Connector error if there is an error
        except ServerError as e:
            raise AmadeusServerError from e
        except ClientError as e:
            raise AmadeusBadRequest from e
        except NotFoundError as e:
            raise AmadeusNothingFound from e

        # extract the dictionaries of the response and save
        # them to the bookshelf if available.
        if 'dictionaries' in response.result.keys():
            self.__bookshelf.add(**response.result['dictionaries'])

        # extract offers from response
        offers = response.result['data']

        # save original amadeus offers to use them later to
        # return details or request seatmaps.
        hashes = self.__offer_cache.add(offers)

        # return the hash values of the offers that match the
        # searchcriteria.
        return hashes

    @timed_lru_cache
    def get(self: object, **params: dict) -> list:
        """
        Search offers that match the given parameters.

        Args:
            self (object): Object itself.
            **params (dict): Analog to the parameters of the following endpoint:
                             https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search/api-reference

        Raises:
            AmadeusNothingFound: There are no offers matching the parameters.
            AmadeusBadRequest: Client did not provide the right parameters.
            AmadeusServerError: Amadeus experienced a server error.

        Returns:
            list: Simplified offers.
        """

        # load the results and get the corresponding
        # hashes to access the results.
        hashes = self.__load_results(**params)

        # get the offer from the cache
        # hint: this method can raise AmadeusNotFound
        # (letting the error propagate higher in the call
        # stack is intended --> don't catch)
        offers = self.__offer_cache.get(hashes)

        # return the simplified offers.
        return self.__simplify_offer(offers)

    def __simplify_offer(self: object, offers: dict) -> list:
        """
        Transform offers to the specified format for search results.

        Args:
        self (object): Object itself.
            offers (dict): Offers with hash value as key.

        Returns:
            list: Simplified offers.
        """

        # create list to return in the end
        slim_offers = list()

        # iterate through all offers
        for key, offer in offers.items():

            # make a deepcopy to prevent changing the
            # originals in place.
            offer = deepcopy(offer)

            # save the segment ids belonging to an
            # itinerary within the itinerary itself
            for i in offer['itineraries']:
                segments = list()
                for s in i['segments']:
                    segments.append(s['id'])
                i['segment_ids'] = segments
                # create a class attribute in each itinerary
                # for later use
                i['classes'] = set()

            # determine which classes are included
            # in each itinerary
            for tp in offer['travelerPricings']:
                for s in tp['fareDetailsBySegment']:
                    for i in offer['itineraries']:
                        if s['segmentId'] in i['segment_ids']:
                            i['classes'].add(s['cabin'])

            # determine pricing
            currency = self.__bookshelf.get(
                'currencies', offer['price']['currency'])
            price = offer['price']['grandTotal']

            # finally bring all into the expected format and
            # add it to the output list.
            slim_offers.append({
                'hash': key,
                'price': {
                    'value': float(price),
                    'currency': currency,
                },
                'itineraries': [
                    {
                        'duration': duration_to_minutes(i['duration']),
                        'stops': len(i['segments']) - 1,
                        'classes': list(i['classes']),
                        'carriers': [
                            {
                                'carrierCode': carrier_code,
                                'carrier': self.__bookshelf.get('carriers', carrier_code),
                            } for carrier_code in set([s['carrierCode'] for s in i['segments']])
                        ],
                        'departure': {
                            'airport': self.__airport.details(i['segments'][0]['departure']['iataCode']),
                            'at': i['segments'][0]['departure']['at'],
                        },
                        'arrival': {
                            'airport': self.__airport.details(i['segments'][-1]['arrival']['iataCode']),
                            'at': i['segments'][-1]['arrival']['at'],
                        },
                    } for i in offer['itineraries']
                ],
            })

        # return the prepared list of simplified offers.
        return slim_offers
