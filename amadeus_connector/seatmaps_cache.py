import json
from fluginfo.settings import BASE_DIR, DEBUG
from os import path
from .errors import AmadeusNothingFound


class SeatmapsCache:

    # TODO: ist ein Cache für Seatmaps sinnvoll?

    def __init__(self: object):
        self.__seatmaps = dict()
    
    def add(self: object, hash: str, seatmap: dict):
        self.__seatmaps[hash] = seatmap

        # write dict as json to file
        if DEBUG:
            json_path = path.join(BASE_DIR, 'amadeus_connector', 'seatmap_cache.json')
            with open(json_path, 'w+') as f:
                json.dump(self.__seatmaps, f, indent=4)
    
    def get(self: object, hash: str) -> dict:

        # TODO: Zeile entfernen wenn Seatmap Cache gewünscht
        raise AmadeusNothingFound
        
        # load from cached seatmaps
        try:
            return self.__seatmaps[hash]
        except KeyError:
            raise AmadeusNothingFound
