import unittest
from unittest.mock import Mock
from amadeus.client.errors import ServerError, ClientError, NotFoundError
from tests.amadeus_client_mock import AmadeusMockClient
from amadeus_connector.airports import Airport
from amadeus_connector.bookshelf import Bookshelf
from amadeus_connector.errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError


class TestAirport(unittest.TestCase):

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.bookshelf = Bookshelf()
        self.airport = Airport(self.amadeus_client, self.bookshelf)

    def test_search_success(self):
        self.assertListEqual(self.airport.search(""), [])
        self.assertListEqual(self.airport.search(
            "London"), AIRPORT_SEARCH_SUCCESS)
        self.assertListEqual(self.airport.search(
            "LHR", is_iata=True), AMADEUS_SEARCH_IATA_SUCCESS)

    def test_search_error(self):
        # Server error
        self.amadeus_client.reference_data.locations.get = Mock(
            side_effect=ServerError(None))
        with self.assertRaises(AmadeusServerError):
            self.airport.search("London")
        # Client error
        self.amadeus_client.reference_data.locations.get = Mock(
            side_effect=ClientError(None))
        with self.assertRaises(AmadeusBadRequest):
            self.airport.search("London")
        # Server error
        self.amadeus_client.reference_data.locations.get = Mock(
            side_effect=NotFoundError(None))
        with self.assertRaises(AmadeusNothingFound):
            self.airport.search("London")

    def test_bookshelf_update(self):
        with self.assertRaises(AmadeusNothingFound):
            self.bookshelf.get("airports", "LHR")
        self.airport.search("London")
        self.assertDictEqual(self.bookshelf.get(
            "airports", "LHR"), AIRPORT_SEARCH_SUCCESS[0])


if __name__ == '__main__':
    unittest.main()

AIRPORT_SEARCH_SUCCESS = [
    {
        "iata": "LHR",
        "name": "HEATHROW",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "LGW",
        "name": "GATWICK",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "STN",
        "name": "STANSTED",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "LTN",
        "name": "LUTON",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "LCY",
        "name": "CITY AIRPORT",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "LYX",
        "name": "LONDON ASHFORD",
        "city": "LYDD",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "SEN",
        "name": "SOUTHEND",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "BQH",
        "name": "BIGGIN HILL",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    },
    {
        "iata": "GON",
        "name": "AIRPORT",
        "city": "GROTON NEW LONDON",
        "countryCode": "US",
        "country": "UNITED STATES OF AMERICA",
        "timezone": "-05:00"
    },
    {
        "iata": "LOZ",
        "name": "MAGEE FIELD",
        "city": "LONDON/CORBIN",
        "countryCode": "US",
        "country": "UNITED STATES OF AMERICA",
        "timezone": "-05:00"
    }
]

AMADEUS_SEARCH_IATA_SUCCESS = [
    {
        "iata": "LHR",
        "name": "HEATHROW",
        "city": "LONDON",
        "countryCode": "GB",
        "country": "UNITED KINGDOM",
        "timezone": "+00:00"
    }
]
