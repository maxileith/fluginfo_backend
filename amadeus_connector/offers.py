from datetime import date
from .foundation import offer_cache, amadeus_client, bookshelf
from .utils import split_duration, inches_to_cm
from .airports import Airport
from amadeus.client.errors import ResponseError
import time
from .errors import AmadeusBadRequest, AmadeusNothingFound
import json
from copy import copy


class OfferSeatmap:

    def __init__(self: object, hash: str, segment_id: int) -> object:
        self.__hash = hash
        self.__segment_id = segment_id

    def get(self: object) -> dict:
        offer = offer_cache.get([self.__hash])[self.__hash]
        response = amadeus_client.shopping.seatmaps.post(
            {
                'data': [offer]
            }
        )
        seatmaps = response.result['data']
        dictionaries = response.result['dictionaries']
        bookshelf.add(**dictionaries)

        # in the var "seatmaps" are now all seatmaps of the
        # given order associated with self.__hash

        return self.__simplify_seatmap(seatmaps)

    def __simplify_seatmap(self: object, seatmaps: list) -> dict:
        try:
            seatmap = list(
                filter(lambda m: m['segmentId'] == self.__segment_id, seatmaps))[0]
        except IndexError:
            raise AmadeusNothingFound

        # create the simplified seatmap
        simplified_seatmap = dict()

        # provide cabin amenities
        aircraftCabinAmenities = seatmap['aircraftCabinAmenities']

        # get information about the seat
        legSpaceUnit = aircraftCabinAmenities['seat']['spaceUnit']
        legSpaceValue = aircraftCabinAmenities['seat']['legSpace']
        legSpace = legSpaceValue if legSpaceUnit == 'CENTIMENTERS' else inches_to_cm(
            legSpaceValue)

        amenities = {
            'power': {
                'isChargeable': aircraftCabinAmenities['power']['isChargeable'],
                'type': bookshelf.get('aircraftCabinAmenitiesPower', aircraftCabinAmenities['power']['powerType']),
            },
            'seat': {
                'legSpace': f'{legSpace} cm',
                'tilt': bookshelf.get('aircraftCabinAmenitiesSeatTilt', aircraftCabinAmenities['seat']['tilt']),
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
                'type': bookshelf.get('aircraftCabinAmenitiesWifi', aircraftCabinAmenities['wifi']['wifiCoverage']),
            },
            'entertainment': [
                {
                    'isChargeable': e['isChargeable'],
                    'type': bookshelf.get('aircraftCabinAmenitiesEntertainment', e['entertainmentType']),
                } for e in aircraftCabinAmenities['entertainment']
            ],
            'food': {
                'isChargeable': aircraftCabinAmenities['food']['isChargeable'],
                'type': bookshelf.get('aircraftCabinAmenitiesFood', aircraftCabinAmenities['food']['foodType']),
            },
            'beverage': {
                'isChargeable': aircraftCabinAmenities['beverage']['isChargeable'],
                'type': bookshelf.get('aircraftCabinAmenitiesBeverage', aircraftCabinAmenities['beverage']['beverageType']),
            },
        }

        simplified_seatmap['amenities'] = amenities

        # make the grid with seat and facility
        # information
        simplified_seatmap['decks'] = list()
        for deck in seatmap['decks']:

            # collect deck_infos about the deck
            deck_infos = {
                'wings': {
                    'startX': deck['deckConfiguration']['startWingsX'],
                    'endX': deck['deckConfiguration']['endWingsX'],
                },
                'seatRows': {
                    'start': deck['deckConfiguration']['startSeatRow'],
                    'end': deck['deckConfiguration']['endSeatRow'],
                },
            }

            # create an empty grid for storing seat and
            # facility information
            width = deck['deckConfiguration']['width']
            length = deck['deckConfiguration']['length']
            row = [None] * width
            grid = list()
            for i in range(0, length, 1):
                grid.append(copy(row))

            # fill the grid up with seats
            for seat in deck['seats']:
                try:
                    x = seat['coordinates']['x']
                    y = seat['coordinates']['y']
                except KeyError:
                    continue

                grid[x][y] = {
                    'type': 'seat',
                    'number': seat['number'],
                    'available': seat['travelerPricing'][0]['seatAvailabilityStatus'] == "AVAILABLE",
                    'characteristics': [
                        bookshelf.get('seatCharacteristics', c) for c in seat['characteristicsCodes']
                    ],
                }

            # fill the seats up with facilities
            for facility in deck['facilities']:
                try:
                    x = facility['coordinates']['x']
                    y = facility['coordinates']['y']
                except KeyError:
                    continue

                grid[x][y] = {
                    'type': 'facility',
                    'name': bookshelf.get('facilities', facility['code']),
                }

            # add deck to the seatmaps
            simplified_seatmap['decks'].append({**deck_infos, 'grid': grid})

        return simplified_seatmap


class OfferDetails:

    def __init__(self: object, hash: str) -> object:
        self.__hash = hash

    def get(self: object) -> dict:
        offer = offer_cache.get([self.__hash])[self.__hash]
        return self.__simplify_offer(offer)

    def __simplify_offer(self: object, offer: dict) -> dict:

        currency = bookshelf.get('currencies', offer['price']['currency'])

        return {
            #'price': {
            #    'total': f'{offer["price"]["total"]} {currency}',
            #    'base': f'{offer["price"]["base"]} {currency}',
            #    'fees': [
            #        {
            #            'amount': f'{f["amount"]} {currency}',
            #            'type': f['type'],
            #        } for f in offer['price']['fees']
            #    ],
            #    'grandTotal': f'{offer["price"]["grandTotal"]} {currency}',
            #},
            'price': f'{offer["price"]["grandTotal"]} {currency}',
            'itineraries': [
                {
                    'duration': split_duration(i['duration']),
                    'segments': [
                        {
                            'id': s['id'],
                            'departure': {
                                'airport': Airport.details(s['departure']['iataCode']),
                                'at': s['departure']['at'],
                            },
                            'arrival': {
                                'airport': Airport.details(s['arrival']['iataCode']),
                                'at': s['arrival']['at'],
                            },
                            'flightNumber': s['carrierCode'] + s['number'],
                            'carrierCode': s['carrierCode'],
                            'carrier': bookshelf.get('carriers', s['carrierCode']),
                            'duration': split_duration(s['duration']),
                            'aircraft': bookshelf.get('aircraft', s['aircraft']['code']),
                            'cabin': list(filter(lambda d: d['segmentId'] == s['id'], offer['travelerPricings'][0]['fareDetailsBySegment']))[0]['cabin'],
                            'class': list(filter(lambda d: d['segmentId'] == s['id'], offer['travelerPricings'][0]['fareDetailsBySegment']))[0]['class'],
                        } for s in i['segments']
                    ],
                } for i in offer['itineraries']
            ],
        }


class OfferSearch:

    def __init__(self: object, **params: dict) -> object:
        self.__params = params

    def mod_filter(self, **params: dict) -> object:
        tmp = {**self.__params, **params}
        # remove key-value-pairs if the value is "None"
        tmp = {k: v for k, v in tmp.items() if v != None}
        self.__params = tmp
        return self

    def __load_results(self: object) -> list:
        try:
            response = amadeus_client.shopping.flight_offers_search.get(
                **self.__params)
        except ResponseError:
            raise AmadeusBadRequest
        # save dictionaries
        dictionaries = response.result['dictionaries']
        bookshelf.add(**dictionaries)
        # cache offers
        offers = response.result['data']
        hashes = offer_cache.add(offers)
        return hashes

    def get(self: object) -> list:
        hashes = self.__load_results()
        # loading the offers from cache to get the hashes
        # and to be uniform with the rest of the code. It
        # would be possible to handle this bit of the code
        # without utilizing the cache.
        offers = offer_cache.get(hashes)
        slim_offers = self.__simplify_offer(offers)
        return slim_offers

    def __simplify_offer(self: object, offers: dict) -> dict:
        slim_offers = {}
        for key, offer in offers.items():

            classes = set()
            for tp in offer['travelerPricings']:
                for s in tp['fareDetailsBySegment']:
                    classes.add(s['cabin'])

            currency = bookshelf.get('currencies', offer['price']['currency'])
            price = offer['price']['grandTotal']

            slim_offers[key] = {
                'price': f'{price} {currency}',
                'classes': list(classes),
                'itineraries': [
                    {
                        'duration': split_duration(i['duration']),
                        'stops': len(i['segments']) - 1,
                        'carriers': [
                            {
                                'carrierCode': carrierCode,
                                'carrier': bookshelf.get('carriers', carrierCode),
                            } for carrierCode in set([s['carrierCode'] for s in i['segments']])
                        ],
                        'departure': {
                            'airport': Airport.details(i['segments'][0]['departure']['iataCode']),
                            'at': i['segments'][0]['departure']['at'],
                        },
                        'arrival': {
                            'airport': Airport.details(i['segments'][-1]['arrival']['iataCode']),
                            'at': i['segments'][-1]['arrival']['at'],
                        },
                    } for i in offer['itineraries']
                ],
            }

        return slim_offers
