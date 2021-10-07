from amadeus import Client
from fluginfo.settings import AMADEUS_KEY, AMADEUS_SECRET
import logging
from .offer_cache import OfferCache
from .bookshelf import Bookshelf

# init amadeus client
amadeus_client = Client(
    client_id=AMADEUS_KEY,
    client_secret=AMADEUS_SECRET,
    logger=logging.Logger,
    log_level='warn',
    hostname='test',
    ssl=True,
)

# offer cache
offer_cache = OfferCache()

# bookshelf
bookshelf = Bookshelf()
