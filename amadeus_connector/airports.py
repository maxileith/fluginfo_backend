from datetime import date
from .foundation import amadeus_client, bookshelf
from amadeus import Location, ResponseError
from .errors import AmadeusNothingFound
from .utils import timed_lru_cache


def simplify_airports(airports: list) -> list:
    return [
        {
            'iata': a['iataCode'],
            'name': a['name'],
            'city': a['address']['cityName'],
            'countryCode': a['address']['countryCode'],
            'country': a['address']['countryName'],
            'timezone': a['timeZoneOffset'],
        }
        for a in airports
    ]


class Airport:

    @staticmethod
    @timed_lru_cache
    def search(s: str, isIata: bool = False) -> list:

        airports = [{'iata': s}] if isIata else []

        if not isIata:
            try:
                response = amadeus_client.reference_data.locations.get(
                    keyword=s,
                    subType=Location.AIRPORT,
                )
                airports = simplify_airports(response.result['data'])
            except ResponseError:
                raise AmadeusNothingFound
        else:
            try:
                response = amadeus_client.reference_data.location(f"A{s}").get()
                airports = simplify_airports([response.result['data']])
            except ResponseError:
                raise AmadeusNothingFound

        bookshelf.add(airports={a['iata']: a for a in airports})
        return airports

    @staticmethod
    def details(iata: str) -> dict:
        try:
            return bookshelf.get('airports', iata)
        except AmadeusNothingFound:
            pass

        # search for the IATA-Code, then take a look
        # to the bookshelf again.
        try:
            Airport.search(iata, isIata=True)
        except AmadeusNothingFound:
            pass
        return bookshelf.get('airports', iata)
