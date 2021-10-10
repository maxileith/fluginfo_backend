from datetime import date
from .foundation import offer_cache, amadeus_client, bookshelf
from .utils import split_duration
from .airports import Airport
from amadeus.client.errors import ResponseError
import time
from .errors import AmadeusBadRequest, AmadeusNothingFound
import json

class OfferSeatmaps:
    
    def __init__(self: object, hash: str) -> object:
        self.__hash = hash

    def get(self: object) -> dict:
        offer = offer_cache.get([self.__hash])[self.__hash]

        print(json.dumps(offer))

        response = amadeus_client.post(
            path='/v1/shopping/seatmaps',
            params={
                'data': [offer]
            }
        )
        return response.result


class OfferDetails:

    def __init__(self: object, hash: str) -> object:
        self.__hash = hash

    def get(self: object) -> dict:
        offer = offer_cache.get([self.__hash])[self.__hash]
        return self.__simplify_offer(offer)

    def __simplify_offer(self: object, offer: dict) -> dict:

        currency = bookshelf.get('currencies', offer['price']['currency'])

        return {
            'price': {
                'total': f'{offer["price"]["total"]} {currency}',
                'base': f'{offer["price"]["base"]} {currency}',
                'fees': [
                    {
                        'amount': f'{f["amount"]} {currency}',
                        'type': f['type'],
                    } for f in offer['price']['fees']
                ],
                'grandTotal': f'{offer["price"]["grandTotal"]} {currency}',
                'perTraveler': {
                    t['travelerId']: {
                        'fareOption': t['fareOption'],
                        'travelerType': t['travelerType'],
                        'price': {
                            'total': f'{t["price"]["total"]} {currency}',
                            'base': f'{t["price"]["base"]} {currency}',
                        },
                    } for t in offer['travelerPricings']
                },
            },
            'itineraries': [
                {
                    'duration': split_duration(i['duration']),
                    'segments': [
                        {
                            'id': s['id'],
                            'departure': {
                                'airport': Airport.details(s['departure']['iataCode']),
                                'at': s['departure']['at'],
                                'terminal': s['departure']['terminal'],
                            },
                            'arrival': {
                                'airport': Airport.details(s['arrival']['iataCode']),
                                'at': s['arrival']['at'],
                                'terminal': s['arrival']['terminal'],
                            },
                            'carrierCode': s['carrierCode'],
                            'carrier': bookshelf.get('carriers', s['carrierCode']),
                            'duration': split_duration(s['duration']),
                            'aircraft': bookshelf.get('aircraft', s['aircraft']['code']),
                            'detailsPerTraveler': {
                                t['travelerId']: {
                                    'cabin': d['cabin'],
                                    'class': d['class'],
                                    'includedCheckedBags': d['includedCheckedBags'] if 'includedCheckedBags' in d.keys() else {},
                                } for t in offer['travelerPricings'] for d in t['fareDetailsBySegment'] if d['segmentId'] == s['id']
                            }
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

    def go(self: object) -> list:
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
