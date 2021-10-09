from datetime import date
from .foundation import amadeus_client, bookshelf
from amadeus import Location, ResponseError


def simplify_airports(airports: list) -> dict:
    return {
        a['iataCode']: {
            'iata': a['iataCode'],
            'name': a['name'],
            'city': a['address']['cityName'],
            'countryCode': a['address']['countryCode'],
            'country': a['address']['countryName'],
            'timezone': a['timeZoneOffset'],
        }
        for a in airports
    }


class Airport:

    @staticmethod
    def search(s: str, isIata: bool = False) -> list:
        airports = {}
        try:
            response = amadeus_client.reference_data.locations.get(
                keyword=s,
                subType=Location.AIRPORT,
            )
            airports = simplify_airports(response.result['data'])
        except ResponseError:
            if isIata:
                airports = {s: {'iata': s}}
        finally:
            bookshelf.add(airports=airports)
            return airports

    @staticmethod
    def details(iata: str) -> dict:
        try:
            return bookshelf.get('airports', iata)
        except KeyError:
            pass

        Airport.search(iata, isIata=True)
        try:
            return bookshelf.get('airports', iata)
        except KeyError:
            pass

        return {}
