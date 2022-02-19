from os import path
import logging
from amadeus import Client
from .offer_cache import OfferCache
from .bookshelf import Bookshelf
from .airports import Airport
from .flightroute import FlightRoute
from .offers import OfferSeatmap, OfferDetails, OfferSearch
from .status import StatusExact, StatusSearch, StatusSeatmap, StatusTimings
from .utils import AIRCRAFT_CABIN_AMENITIES

# in this file are variables that are required by
# almost all components of the amadeus connector.


class AmadeusConnector:
    """
    Everything that is needed for providing the required information for the Fluginfo website.
    """

    def __init__(self: object, client_id: str, client_secret: str, prod: bool = False, logger: object = logging.Logger, ssl: bool = True, debug: bool = False, debug_output_path: str = path.dirname(path.realpath(__file__))) -> object:
        """
        Initialize the connector.

        Args:
            self (object): Object itself.
            client_id (str): Amadeus API key.
            client_secret (str): Amadeus API secret.
            prod (bool, optional): Use production or test Amadeus API. Defaults to False.
            logger (object, optional): Logger. Defaults to logging.Logger.
            ssl (bool, optional): Use TLS encryption. Defaults to True.
            debug (bool, optional): Write bookshelf and offer cache to json files for debugging. Defaults to False.
            debug_output_path (str, optional): Path of debugging files. Defaults to path.dirname(path.realpath(__file__)).

        Returns:
            object: Amadeus connector.
        """

        self.__amadeus_client = Client(
            client_id=client_id,
            client_secret=client_secret,
            logger=logger,
            hostname='production' if prod else 'test',
            ssl=ssl,
        )

        # offer cache
        self.__offer_cache = OfferCache(
            debug=debug,
            debug_output_path=debug_output_path,
        )

        # init bookshelf with the aircraft cabin amenities since
        # these are not provided within the responses of amadeus
        # responses
        self.__bookshelf = Bookshelf(
            initial_dictionaries=AIRCRAFT_CABIN_AMENITIES,
            debug=debug,
            debug_output_path=debug_output_path,
        )

        self.airport = Airport(
            amadeus_client=self.__amadeus_client,
            bookshelf=self.__bookshelf,
        )

        self.flight_route = FlightRoute(self.__amadeus_client)

        self.offer_search = OfferSearch(
            amadeus_client=self.__amadeus_client,
            bookshelf=self.__bookshelf,
            offer_cache=self.__offer_cache,
        )

        self.offer_details = OfferDetails(
            amadeus_client=self.__amadeus_client,
            bookshelf=self.__bookshelf,
            offer_cache=self.__offer_cache,
        )

        self.offer_seatmap = OfferSeatmap(
            amadeus_client=self.__amadeus_client,
            bookshelf=self.__bookshelf,
            offer_cache=self.__offer_cache,
        )

        self.status_search = StatusSearch(
            amadeus_client=self.__amadeus_client,
            bookshelf=self.__bookshelf
        )

        self.status_exact = StatusExact(
            amadeus_client=self.__amadeus_client,
            bookshelf=self.__bookshelf,
        )

        self.status_seatmap = StatusSeatmap(
            amadeus_client=self.__amadeus_client,
            bookshelf=self.__bookshelf,
            offer_cache=self.__offer_cache,
        )

        self.status_timings = StatusTimings(self.__amadeus_client)
