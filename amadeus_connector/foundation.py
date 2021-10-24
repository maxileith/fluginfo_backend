from amadeus import Client
from fluginfo.settings import AMADEUS_KEY, AMADEUS_SECRET
import logging
from .offer_cache import OfferCache
from .seatmaps_cache import SeatmapsCache
from .bookshelf import Bookshelf

# init amadeus client
amadeus_client = Client(
    client_id=AMADEUS_KEY,
    client_secret=AMADEUS_SECRET,
    logger=logging.Logger,
    hostname='test',
    ssl=True,
)

# offer cache
offer_cache = OfferCache()

# seatmap cache
seatmaps_cache = SeatmapsCache()

AIRCRAFT_CABIN_AMENITIES = {
    'aircraftCabinAmenitiesPower': {
        'PLUG': 'Plug',
        'USB_PORT': 'USB-Port',
        'ADAPTOR': 'Adaptor',
        'PLUG_OR_USB_PORT': 'Plug or USB-Port',
    },
    'aircraftCabinAmenitiesSeatTilt': {
        'FULL_FLAT': 'Full flat',
        'ANGLE_FLAT': 'Angled flat',
        'NORMAL': 'Normal',
    },
    'aircraftCabinAmenitiesWifi': {
        'FULL': 'Full',
        'PARTIAL': 'Partial',
    },
    'aircraftCabinAmenitiesEntertainment': {
        'LIVE_TV': 'Live-TV',
        'MOVIES': 'Movies',
        'AUDIO_VIDEO_ON_DEMAND': 'Audio & Video on demand',
        'TV_SHOWS': 'TV-Shows',
        'IP_TV': 'IP-TV',
    },
    'aircraftCabinAmenitiesFood': {
        'MEAL': 'Meal',
        'FRESH_MEAL': 'Fresh meal',
        'SNACK': 'Snacks',
        'FRESH_SNACK': 'Fresh snacks',
    },
    'aircraftCabinAmenitiesBeverage': {
        'ALCOHOLIC': 'Alcoholic',
        'NON_ALCOHOLIC': 'Non-Alcoholic',
        'ALCOHOLIC_AND_NON_ALCOHOLIC': 'With and without alcohol',
    },
}

# bookshelf
bookshelf = Bookshelf(AIRCRAFT_CABIN_AMENITIES)
