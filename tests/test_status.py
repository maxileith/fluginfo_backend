import unittest
from copy import deepcopy
from unittest.mock import Mock
from amadeus.client.errors import ServerError, ClientError, NotFoundError
from tests.amadeus_client_mock import AmadeusMockClient
from tests.test_offers import OFFER_SEATMAP_RESULT
from amadeus_connector.status import StatusExact, StatusSearch, StatusSeatmap
from amadeus_connector.errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from amadeus_connector.bookshelf import Bookshelf
from amadeus_connector.offer_cache import OfferCache
from tests.test_offers import INITIAL_DICTIONARIES


class TestStatusSearch(unittest.TestCase):

    PARAMS = {
        'departure_iata': 'FRA',
        'arrival_iata': 'DFW',
        'date': '2022-03-01',
    }

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.bookshelf = Bookshelf()
        self.status_search = StatusSearch(
            amadeus_client=self.amadeus_client,
            bookshelf=self.bookshelf,
        )

    def test_get_success(self):
        self.assertListEqual(
            STATUS_SEARCH_RESULTS,
            self.status_search.get(**self.PARAMS),
        )

    def test_get_error(self):
        # server error
        self.amadeus_client.shopping.availability.flight_availabilities.post = Mock(
            side_effect=ServerError(None))
        with self.assertRaises(AmadeusServerError):
            self.status_search.get(**self.PARAMS)
        # client error
        self.amadeus_client.shopping.availability.flight_availabilities.post = Mock(
            side_effect=ClientError(None))
        with self.assertRaises(AmadeusBadRequest):
            self.status_search.get(**self.PARAMS)
        # nothing found
        self.amadeus_client.shopping.availability.flight_availabilities.post = Mock(
            side_effect=NotFoundError(None))
        with self.assertRaises(AmadeusNothingFound):
            self.status_search.get(**self.PARAMS)


class TestStatusExact(unittest.TestCase):

    PARAMS = {
        'flight_number': 'LH438',
        'date': '2022-03-01',
    }

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.bookshelf = Bookshelf(INITIAL_DICTIONARIES)
        self.status_exact = StatusExact(
            amadeus_client=self.amadeus_client,
            bookshelf=self.bookshelf,
        )

    def test_get_success(self):
        self.assertDictEqual(STATUS_DETAILS_RESULT,
                             self.status_exact.get(**self.PARAMS))

    def test_get_error(self):
        # server error
        self.amadeus_client.shopping.availability.flight_availabilities.post = Mock(
            side_effect=ServerError(None))
        with self.assertRaises(AmadeusServerError):
            self.status_exact.get(**self.PARAMS)
        # client error
        self.amadeus_client.shopping.availability.flight_availabilities.post = Mock(
            side_effect=ClientError(None))
        with self.assertRaises(AmadeusBadRequest):
            self.status_exact.get(**self.PARAMS)
        # nothing found
        self.amadeus_client.shopping.availability.flight_availabilities.post = Mock(
            side_effect=NotFoundError(None))
        with self.assertRaises(AmadeusNothingFound):
            self.status_exact.get(**self.PARAMS)


class TestStatusSeatmap(unittest.TestCase):

    PARAMS = {
        'flight_number': 'LH438',
        'date': '2022-03-01',
        'travel_class': 'Y',
    }

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.bookshelf = Bookshelf(INITIAL_DICTIONARIES)
        self.offer_cache = OfferCache()
        self.status_seatmap = StatusSeatmap(
            amadeus_client=self.amadeus_client,
            bookshelf=self.bookshelf,
            offer_cache=self.offer_cache,
        )

    def test_get_success(self):
        expected = deepcopy(OFFER_SEATMAP_RESULT)
        del OFFER_SEATMAP_RESULT['aircraft']
        self.assertDictEqual(OFFER_SEATMAP_RESULT,
                             self.status_seatmap.get(**self.PARAMS))


if __name__ == '__main__':
    unittest.main()

STATUS_SEARCH_RESULTS = [
    {
        "flightNumber": "UA8864",
        "carrierCode": "UA",
        "departure": {
            "airport": {
                "iata": "FRA"
            },
            "at": "2022-03-01T09:55:00"
        },
        "arrival": {
            "airport": {
                "iata": "DFW"
            },
            "at": "2022-03-01T14:15:00"
        },
        "duration": 680,
        "aircraft": "333",
        "availableSeats": [
            {
                "classId": "J",
                "seats": 4
            },
            {
                "classId": "C",
                "seats": 4
            },
            {
                "classId": "D",
                "seats": 4
            },
            {
                "classId": "Z",
                "seats": 4
            },
            {
                "classId": "O",
                "seats": 6
            },
            {
                "classId": "A",
                "seats": 6
            },
            {
                "classId": "R",
                "seats": 6
            },
            {
                "classId": "Y",
                "seats": 6
            },
            {
                "classId": "B",
                "seats": 6
            },
            {
                "classId": "M",
                "seats": 6
            },
            {
                "classId": "U",
                "seats": 6
            },
            {
                "classId": "H",
                "seats": 6
            },
            {
                "classId": "Q",
                "seats": 6
            },
            {
                "classId": "V",
                "seats": 6
            },
            {
                "classId": "W",
                "seats": 6
            },
            {
                "classId": "S",
                "seats": 6
            },
            {
                "classId": "T",
                "seats": 6
            }
        ]
    },
    {
        "flightNumber": "LH438",
        "carrierCode": "LH",
        "departure": {
            "airport": {
                "iata": "FRA"
            },
            "at": "2022-03-01T09:55:00"
        },
        "arrival": {
            "airport": {
                "iata": "DFW"
            },
            "at": "2022-03-01T14:15:00"
        },
        "duration": 680,
        "aircraft": "333",
        "availableSeats": [
            {
                "classId": "J",
                "seats": 9
            },
            {
                "classId": "C",
                "seats": 9
            },
            {
                "classId": "D",
                "seats": 9
            },
            {
                "classId": "Z",
                "seats": 9
            },
            {
                "classId": "G",
                "seats": 9
            },
            {
                "classId": "E",
                "seats": 9
            },
            {
                "classId": "Y",
                "seats": 9
            },
            {
                "classId": "B",
                "seats": 9
            },
            {
                "classId": "M",
                "seats": 9
            },
            {
                "classId": "U",
                "seats": 9
            },
            {
                "classId": "H",
                "seats": 9
            },
            {
                "classId": "Q",
                "seats": 9
            },
            {
                "classId": "V",
                "seats": 9
            },
            {
                "classId": "W",
                "seats": 9
            },
            {
                "classId": "S",
                "seats": 9
            },
            {
                "classId": "T",
                "seats": 9
            }
        ]
    },
    {
        "flightNumber": "IB4203",
        "carrierCode": "IB",
        "departure": {
            "airport": {
                "iata": "FRA"
            },
            "at": "2022-03-01T10:50:00"
        },
        "arrival": {
            "airport": {
                "iata": "DFW"
            },
            "at": "2022-03-01T15:00:00"
        },
        "duration": 670,
        "aircraft": "787",
        "availableSeats": [
            {
                "classId": "J",
                "seats": 7
            },
            {
                "classId": "C",
                "seats": 7
            },
            {
                "classId": "D",
                "seats": 7
            },
            {
                "classId": "R",
                "seats": 7
            },
            {
                "classId": "I",
                "seats": 7
            },
            {
                "classId": "W",
                "seats": 7
            },
            {
                "classId": "E",
                "seats": 7
            },
            {
                "classId": "T",
                "seats": 7
            },
            {
                "classId": "Y",
                "seats": 7
            },
            {
                "classId": "B",
                "seats": 7
            },
            {
                "classId": "H",
                "seats": 7
            },
            {
                "classId": "K",
                "seats": 7
            },
            {
                "classId": "M",
                "seats": 7
            },
            {
                "classId": "L",
                "seats": 7
            },
            {
                "classId": "V",
                "seats": 7
            },
            {
                "classId": "S",
                "seats": 7
            },
            {
                "classId": "N",
                "seats": 7
            },
            {
                "classId": "Q",
                "seats": 7
            },
            {
                "classId": "O",
                "seats": 7
            }
        ]
    }
]

STATUS_DETAILS_RESULT = {
    "flightNumber": "LH438",
    "carrierCode": "LH",
    "departure": {
        "airport": {
            "iata": "FRA",
            "name": "FRANKFURT INTL",
            "city": "FRANKFURT",
            "countryCode": "DE",
            "country": "GERMANY",
            "timezone": "+01:00"
        },
        "at": "2022-03-01T09:55:00"
    },
    "arrival": {
        "airport": {
            "iata": "DFW",
            "name": "DALLAS FT WORTH INTL",
            "city": "DALLAS",
            "countryCode": "US",
            "country": "UNITED STATES OF AMERICA",
            "timezone": "-06:00"
        },
        "at": "2022-03-01T14:15:00"
    },
    "duration": 680,
    "aircraft": "333",
    "availableSeats": [
        {
            "classId": "J",
            "seats": 9
        },
        {
            "classId": "C",
            "seats": 9
        },
        {
            "classId": "D",
            "seats": 9
        },
        {
            "classId": "Z",
            "seats": 9
        },
        {
            "classId": "G",
            "seats": 9
        },
        {
            "classId": "E",
            "seats": 9
        },
        {
            "classId": "Y",
            "seats": 9
        },
        {
            "classId": "B",
            "seats": 9
        },
        {
            "classId": "M",
            "seats": 9
        },
        {
            "classId": "U",
            "seats": 9
        },
        {
            "classId": "H",
            "seats": 9
        },
        {
            "classId": "Q",
            "seats": 9
        },
        {
            "classId": "V",
            "seats": 9
        },
        {
            "classId": "W",
            "seats": 9
        },
        {
            "classId": "S",
            "seats": 9
        },
        {
            "classId": "T",
            "seats": 9
        }
    ]
}
