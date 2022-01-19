from datetime import date
from .foundation import amadeus_client, bookshelf
from amadeus import Location
from amadeus.client.errors import ResponseError, ServerError, ClientError, NotFoundError
from .errors import AmadeusNothingFound, AmadeusBadRequest, AmadeusServerError
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

        if s == "":
            return []

        airports = [{'iata': s}] if isIata else []

        try:
            if not isIata:
                response = amadeus_client.reference_data.locations.get(
                    keyword=s,
                    subType=Location.AIRPORT,
                )
                airports = simplify_airports(response.result['data'])
            else:
                response = amadeus_client.reference_data.location(f"A{s}").get()
                airports = simplify_airports([response.result['data']])
        except ServerError:
            raise AmadeusServerError
        except ClientError:
            raise AmadeusBadRequest
        except NotFoundError:
            raise AmadeusNothingFound
        finally:
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
        except (AmadeusNothingFound or AmadeusBadRequest):
            pass
        return bookshelf.get('airports', iata)
