from fluginfo.settings import BASE_DIR, DEBUG
from os import path
import json
from .errors import AmadeusNothingFound

class Bookshelf:

    def __init__(self: object, initial_dictionaries: dict):
        self.__dictionaries = initial_dictionaries

    def add(self: object, **dictionaries: dict):
        # aircraft, locations, currencies, ...
        all_types = list(dictionaries.keys())
        all_types.extend(self.__dictionaries.keys())
        all_types = set(all_types)

        for t in all_types:
            if t in self.__dictionaries.keys() and t in dictionaries.keys():
                # combine e.g. the aircrafts from both dictionairies
                self.__dictionaries[t] = {**dictionaries[t], **self.__dictionaries[t]}
            elif t in dictionaries.keys():
                self.__dictionaries[t] = dictionaries[t]

        # write dict as json to file
        if DEBUG:
            json_path = path.join(BASE_DIR, 'amadeus_connector', 'bookshelf.json')
            with open(json_path, 'w+') as f:
                json.dump(self.__dictionaries, f, indent=4)

    def get(self: object, type: str, id: str) -> dict:
        try:
            return self.__dictionaries[type][id]
        except KeyError:
            raise AmadeusNothingFound
