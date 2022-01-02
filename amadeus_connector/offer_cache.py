import json
from fluginfo.settings import BASE_DIR, DEBUG
from os import path
from hashlib import sha512
from .errors import AmadeusNothingFound


class OfferCache:

    def __init__(self: object, initial_offers: dict = {}) -> object:
        self.__offers = initial_offers

    def add(self: object, offers: list) -> list:
        keys_added = []
        for offer in offers:
            as_string = json.dumps(offer, sort_keys=True)
            hash_value = sha512(as_string.encode('utf-8')).hexdigest()
            self.__offers[hash_value] = offer
            keys_added.append(hash_value)

        # write dict as json to file
        if DEBUG:
            json_path = path.join(
                BASE_DIR, 'amadeus_connector', 'offer_cache.json')
            with open(json_path, 'w+') as f:
                json.dump(self.__offers, f, indent=4)

        return keys_added

    def get(self: object, hash_values: list, ignore_missing: bool = False) -> dict:
        offers = dict()

        # load from cached offers
        for h in hash_values:
            try:
                offers[h] = self.__offers[h]
            except KeyError:
                if not ignore_missing:
                    raise AmadeusNothingFound

        return offers
