import amadeus
from amadeus import Location
from amadeus.client.errors import ServerError, ClientError, NotFoundError
from .errors import AmadeusNothingFound, AmadeusBadRequest, AmadeusServerError
from .utils import timed_lru_cache
from .bookshelf import Bookshelf


def simplify_airports(airports: list) -> list:
    """
    This function converts a list of airports into the specified format.

    Args:
        airports (list): airports to convert

    Returns:
        list: list of converted airports
    """
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
    """
    This class contains methods intended for requesting airport information.
    """

    def __init__(self, amadeus_client: amadeus.Client, bookshelf: Bookshelf) -> object:
        """
        Initialize airport object.

        Args:
            self (object): Object itself.
            amadeus_client (amadeus.Client): Amadeus client instance.
            bookshelf (Bookshelf): Bookshelf instance.

        Returns:
            object: Airport object.
        """
        self.__amadeus_client = amadeus_client
        self.__bookshelf = bookshelf

    @timed_lru_cache(forever=True)
    def search(self, keyword: str, is_iata: bool = False) -> list:
        """
        Returns airports that match the specified keyword.

        Args:
            self (object): Object itself.
            keyword (str): keyword
            is_iata (bool, optional): Specifies whether the keyword is an IATA code or not. Defaults to False.

        Raises:
            AmadeusServerError: Amadeus experienced a server error.
            AmadeusBadRequest: Client did not provide the right parameters.

        Returns:
            list: airports that match the keyword
        """

        # return an empty list if the keyword is empty
        if keyword == "":
            return []

        airports = [{'iata': keyword}] if is_iata else []

        try:
            if is_iata:
                # if the keyword is an IATA code, just query the details
                # by the code directly instead of searching.
                # A + <IATA>: A for "airport"
                response = self.__amadeus_client.reference_data.location(
                    f"A{keyword}").get()
                # transform to the specified format
                airports = simplify_airports([response.result['data']])
            else:
                # search for the airport by keyword
                response = self.__amadeus_client.reference_data.locations.get(
                    keyword=keyword,
                    subType=Location.AIRPORT,
                )
                # transform to the specified format
                airports = simplify_airports(response.result['data'])
        # return an Amadeus Connector error if there is an error
        except ServerError as e:
            raise AmadeusServerError from e
        except ClientError as e:
            raise AmadeusBadRequest from e
        except NotFoundError as e:
            raise AmadeusNothingFound from e
        finally:
            # Save airport information in the bookshelf, even if no information
            # could be determined, so that no further attempts are made on the
            # keyword in the future.
            self.__bookshelf.add(airports={a['iata']: a for a in airports})

        # return the airports
        return airports

    def details(self, iata: str) -> dict:
        """
        Return the airport that matches a specified IATA code.

        Args:
            self (object): Object itself.
            iata (str): IATA code of the airport, e.g. FRA.

        Returns:
            dict: Details about the airport. Empty if not found.
        """

        # first, look into the bookshelf if there are already details regarding
        # the specified airport
        try:
            return self.__bookshelf.get('airports', iata)
        except AmadeusNothingFound:
            pass

        # if there was nothing found in the bookshelf, trigger the airport search
        # to load details
        try:
            self.search(iata, is_iata=True)
        except AmadeusNothingFound:
            pass
        except AmadeusBadRequest:
            pass

        # at this point there should be information regarding the airport if
        # amadeus knows this airport. Return these. The response could be empty
        # because if there was nothing found within amadeus, an empty entry
        # is made in the dictionary
        return self.__bookshelf.get('airports', iata)
