import unittest
from unittest.mock import Mock
from amadeus.client.errors import ServerError, ClientError, NotFoundError
from tests.amadeus_client_mock import AmadeusMockClient
from amadeus_connector.offers import OfferSearch, OfferDetails, OfferSeatmap
from amadeus_connector.errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from amadeus_connector.bookshelf import Bookshelf
from amadeus_connector.offer_cache import OfferCache
from amadeus_connector.utils import AIRCRAFT_CABIN_AMENITIES


SEARCH_PARAMS = {
    'adults': 1,
    'children': 0,
    'departureDate': '2022-03-01',
    'max': 5,
    'returnDate': '2022-03-08',
    'destinationLocationCode': 'DFW',
    'nonStop': False,
    'originLocationCode': 'MUC',
}


class TestOfferSearch(unittest.TestCase):

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.bookshelf = Bookshelf(INITIAL_DICTIONARIES)
        self.offer_cache = OfferCache()
        self.offer_search = OfferSearch(
            amadeus_client=self.amadeus_client,
            bookshelf=self.bookshelf,
            offer_cache=self.offer_cache,
        )

    def test_get_success(self):
        self.assertListEqual(
            self.offer_search.get(**SEARCH_PARAMS),
            OFFER_SEARCH_RESULTS
        )

    def test_get_error(self):
        # server error
        self.amadeus_client.shopping.flight_offers_search.get = Mock(
            side_effect=ServerError(None))
        with self.assertRaises(AmadeusServerError):
            self.offer_search.get(**SEARCH_PARAMS)
        # client error
        self.amadeus_client.shopping.flight_offers_search.get = Mock(
            side_effect=ClientError(None))
        with self.assertRaises(AmadeusBadRequest):
            self.offer_search.get(**SEARCH_PARAMS)
        # nothing found
        self.amadeus_client.shopping.flight_offers_search.get = Mock(
            side_effect=NotFoundError(None))
        with self.assertRaises(AmadeusNothingFound):
            self.offer_search.get(**SEARCH_PARAMS)


class TestOfferDetails(unittest.TestCase):

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.bookshelf = Bookshelf(INITIAL_DICTIONARIES)
        self.offer_cache = OfferCache(INITIAL_OFFER_CACHE)
        self.offer_details = OfferDetails(
            amadeus_client=self.amadeus_client,
            bookshelf=self.bookshelf,
            offer_cache=self.offer_cache,
        )

    def test_get_success(self):
        self.assertDictEqual(OFFER_DETAILS_RESULT, self.offer_details.get(
            'ccae73216a5865d8605b92c2a04254e83057e1cfd6285483256423c9dac65d9b3cf1fcd155dee77e61286aaba01a4a5f449f2b4fa97476f80f4d115b17b0556e'))

    def test_get_nothing_found(self):
        with self.assertRaises(AmadeusNothingFound):
            self.offer_details.get('abc')


class TestOfferSeatmap(unittest.TestCase):

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.bookshelf = Bookshelf(INITIAL_DICTIONARIES)
        self.offer_cache = OfferCache(INITIAL_OFFER_CACHE)
        self.offer_seatmap = OfferSeatmap(
            amadeus_client=self.amadeus_client,
            bookshelf=self.bookshelf,
            offer_cache=self.offer_cache,
        )

    def test_get_success(self):
        self.assertDictEqual(OFFER_SEATMAP_RESULT, self.offer_seatmap.get(
            'ccae73216a5865d8605b92c2a04254e83057e1cfd6285483256423c9dac65d9b3cf1fcd155dee77e61286aaba01a4a5f449f2b4fa97476f80f4d115b17b0556e', 1))

    def test_get_error(self):
        # server error
        self.amadeus_client.shopping.seatmaps.post = Mock(
            side_effect=ServerError(None))
        with self.assertRaises(AmadeusServerError):
            self.offer_seatmap.get(
                'ccae73216a5865d8605b92c2a04254e83057e1cfd6285483256423c9dac65d9b3cf1fcd155dee77e61286aaba01a4a5f449f2b4fa97476f80f4d115b17b0556e', 1)
        # client error
        self.amadeus_client.shopping.seatmaps.post = Mock(
            side_effect=ClientError(None))
        with self.assertRaises(AmadeusBadRequest):
            self.offer_seatmap.get(
                'ccae73216a5865d8605b92c2a04254e83057e1cfd6285483256423c9dac65d9b3cf1fcd155dee77e61286aaba01a4a5f449f2b4fa97476f80f4d115b17b0556e', 1)
        # nothing found error
        self.amadeus_client.shopping.seatmaps.post = Mock(
            side_effect=NotFoundError(None))
        with self.assertRaises(AmadeusNothingFound):
            self.offer_seatmap.get(
                'ccae73216a5865d8605b92c2a04254e83057e1cfd6285483256423c9dac65d9b3cf1fcd155dee77e61286aaba01a4a5f449f2b4fa97476f80f4d115b17b0556e', 1)

    def test_get_invalid_params(self):
        # invalid segment_id
        with self.assertRaises(AmadeusNothingFound):
            self.offer_seatmap.get(
                'ccae73216a5865d8605b92c2a04254e83057e1cfd6285483256423c9dac65d9b3cf1fcd155dee77e61286aaba01a4a5f449f2b4fa97476f80f4d115b17b0556e', 2)
        # invalid offer
        with self.assertRaises(AmadeusNothingFound):
            self.offer_seatmap.get('abc', 2)


if __name__ == '__main__':
    unittest.main()

INITIAL_DICTIONARIES = {
    "carriers": {
        "AY": "FINNAIR",
    },
    "aircraft": {
        "788": "BOEING 787-8",
    },
    "airports": {
        "FRA": {
            "iata": "FRA",
            "name": "FRANKFURT INTL",
            "city": "FRANKFURT",
            "countryCode": "DE",
            "country": "GERMANY",
            "timezone": "+01:00"
        },
        "DFW": {
            "iata": "DFW",
            "name": "DALLAS FT WORTH INTL",
            "city": "DALLAS",
            "countryCode": "US",
            "country": "UNITED STATES OF AMERICA",
            "timezone": "-06:00"
        },
        "MUC": {
            "iata": "MUC",
            "name": "MUNICH INTERNATIONAL",
            "city": "MUNICH",
            "countryCode": "DE",
            "country": "GERMANY",
            "timezone": "+01:00"
        }
    }
}
INITIAL_DICTIONARIES = {**AIRCRAFT_CABIN_AMENITIES, **INITIAL_DICTIONARIES}

OFFER_SEARCH_RESULTS = [
    {
        "hash": "af5bdd441e3b8cec0ee4b223eb6ba24663f0093b8b3546690482df0a6a3ca11b73f2bd2fc105736b71e7e3e3b4bfbc3c11c059b5c1c6e4a2d074f5b6898353be",
        "price": 781.55,
        "itineraries": [
            {
                "duration": 1008,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "AC",
                        "carrier": "AIR CANADA"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-01T11:50:00"
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
                    "at": "2022-03-01T21:38:00"
                }
            },
            {
                "duration": 709,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "LH",
                        "carrier": "LUFTHANSA"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "DFW",
                        "name": "DALLAS FT WORTH INTL",
                        "city": "DALLAS",
                        "countryCode": "US",
                        "country": "UNITED STATES OF AMERICA",
                        "timezone": "-06:00"
                    },
                    "at": "2022-03-08T17:56:00"
                },
                "arrival": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-09T12:45:00"
                }
            }
        ]
    },
    {
        "hash": "0e85e89cacb4a40dd86bcb569703e05d6064b762e6f981479be2c27975334890a1960eb2dc02fc2f5d8886723e20c45e19c53d063d1326e44364bbcfa2e8a69d",
        "price": 781.55,
        "itineraries": [
            {
                "duration": 1008,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "UA",
                        "carrier": "UNITED AIRLINES"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-01T11:50:00"
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
                    "at": "2022-03-01T21:38:00"
                }
            },
            {
                "duration": 709,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "LH",
                        "carrier": "LUFTHANSA"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "DFW",
                        "name": "DALLAS FT WORTH INTL",
                        "city": "DALLAS",
                        "countryCode": "US",
                        "country": "UNITED STATES OF AMERICA",
                        "timezone": "-06:00"
                    },
                    "at": "2022-03-08T17:56:00"
                },
                "arrival": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-09T12:45:00"
                }
            }
        ]
    },
    {
        "hash": "d416c24bc2f9619fe67ce8c112332cfe83365f0b373ea47f13d47e7420829c39e5749f6208cdfe5ab2cf4e288eb4bbe56edc1a2ac310d3e1059969f6cfe4d613",
        "price": 781.55,
        "itineraries": [
            {
                "duration": 1008,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "AC",
                        "carrier": "AIR CANADA"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-01T11:50:00"
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
                    "at": "2022-03-01T21:38:00"
                }
            },
            {
                "duration": 731,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "UA",
                        "carrier": "UNITED AIRLINES"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "DFW",
                        "name": "DALLAS FT WORTH INTL",
                        "city": "DALLAS",
                        "countryCode": "US",
                        "country": "UNITED STATES OF AMERICA",
                        "timezone": "-06:00"
                    },
                    "at": "2022-03-08T12:29:00"
                },
                "arrival": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-09T07:40:00"
                }
            }
        ]
    },
    {
        "hash": "39bea1419966a36f265175c87563a5daa4c3c5a3a2939612d51bdf540cb262acbf5a330c7672575a7c0e2121a1c30e8292883e8dfafd5da9154f04b73adfa989",
        "price": 781.55,
        "itineraries": [
            {
                "duration": 1008,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "AC",
                        "carrier": "AIR CANADA"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-01T11:50:00"
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
                    "at": "2022-03-01T21:38:00"
                }
            },
            {
                "duration": 754,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "UA",
                        "carrier": "UNITED AIRLINES"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "DFW",
                        "name": "DALLAS FT WORTH INTL",
                        "city": "DALLAS",
                        "countryCode": "US",
                        "country": "UNITED STATES OF AMERICA",
                        "timezone": "-06:00"
                    },
                    "at": "2022-03-08T14:01:00"
                },
                "arrival": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-09T09:35:00"
                }
            }
        ]
    },
    {
        "hash": "726f270686767f36f7c23db328673ead5893bb2feb2c936ff28e56365d7ad4e024d15336fd093efb55af4e962e1b398ec0f07c841eb94258e9e9c9fd9fe4b66c",
        "price": 781.55,
        "itineraries": [
            {
                "duration": 1008,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "AC",
                        "carrier": "AIR CANADA"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-01T11:50:00"
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
                    "at": "2022-03-01T21:38:00"
                }
            },
            {
                "duration": 815,
                "stops": 1,
                "classes": [
                    "ECONOMY"
                ],
                "carriers": [
                    {
                        "carrierCode": "UA",
                        "carrier": "UNITED AIRLINES"
                    }
                ],
                "departure": {
                    "airport": {
                        "iata": "DFW",
                        "name": "DALLAS FT WORTH INTL",
                        "city": "DALLAS",
                        "countryCode": "US",
                        "country": "UNITED STATES OF AMERICA",
                        "timezone": "-06:00"
                    },
                    "at": "2022-03-08T10:45:00"
                },
                "arrival": {
                    "airport": {
                        "iata": "MUC",
                        "name": "MUNICH INTERNATIONAL",
                        "city": "MUNICH",
                        "countryCode": "DE",
                        "country": "GERMANY",
                        "timezone": "+01:00"
                    },
                    "at": "2022-03-09T07:20:00"
                }
            }
        ]
    }
]

INITIAL_OFFER_CACHE = {
    "ccae73216a5865d8605b92c2a04254e83057e1cfd6285483256423c9dac65d9b3cf1fcd155dee77e61286aaba01a4a5f449f2b4fa97476f80f4d115b17b0556e": {
        "type": "flight-offer",
        "id": "1",
        "source": "GDS",
        "instantTicketingRequired": False,
        "nonHomogeneous": False,
        "oneWay": False,
        "lastTicketingDate": "2022-02-20",
        "numberOfBookableSeats": 7,
        "itineraries": [
            {
                "duration": "PT11H10M",
                "segments": [
                    {
                        "departure": {
                            "iataCode": "FRA",
                            "terminal": "2",
                            "at": "2022-03-01T10:50:00"
                        },
                        "arrival": {
                            "iataCode": "DFW",
                            "terminal": "D",
                            "at": "2022-03-01T15:00:00"
                        },
                        "carrierCode": "AY",
                        "number": "5799",
                        "aircraft": {
                            "code": "788"
                        },
                        "operating": {
                            "carrierCode": "AA"
                        },
                        "duration": "PT11H10M",
                        "id": "1",
                        "numberOfStops": 0,
                        "blacklistedInEU": False
                    }
                ]
            },
            {
                "duration": "PT9H30M",
                "segments": [
                    {
                        "departure": {
                            "iataCode": "DFW",
                            "terminal": "0",
                            "at": "2022-03-03T16:00:00"
                        },
                        "arrival": {
                            "iataCode": "FRA",
                            "terminal": "2",
                            "at": "2022-03-04T08:30:00"
                        },
                        "carrierCode": "AY",
                        "number": "5800",
                        "aircraft": {
                            "code": "788"
                        },
                        "operating": {
                            "carrierCode": "AA"
                        },
                        "duration": "PT9H30M",
                        "id": "6",
                        "numberOfStops": 0,
                        "blacklistedInEU": False
                    }
                ]
            }
        ],
        "price": {
            "currency": "EUR",
            "total": "4649.23",
            "base": "3047.00",
            "fees": [
                {
                    "amount": "0.00",
                    "type": "SUPPLIER"
                },
                {
                    "amount": "0.00",
                    "type": "TICKETING"
                }
            ],
            "grandTotal": "4649.23"
        },
        "pricingOptions": {
            "fareType": [
                "PUBLISHED"
            ],
            "includedCheckedBagsOnly": False
        },
        "validatingAirlineCodes": [
            "AY"
        ],
        "travelerPricings": [
            {
                "travelerId": "1",
                "fareOption": "STANDARD",
                "travelerType": "ADULT",
                "price": {
                    "currency": "EUR",
                    "total": "1232.98",
                    "base": "846.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "1",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    },
                    {
                        "segmentId": "6",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    }
                ]
            },
            {
                "travelerId": "2",
                "fareOption": "STANDARD",
                "travelerType": "ADULT",
                "price": {
                    "currency": "EUR",
                    "total": "1232.98",
                    "base": "846.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "1",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    },
                    {
                        "segmentId": "6",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    }
                ]
            },
            {
                "travelerId": "3",
                "fareOption": "STANDARD",
                "travelerType": "CHILD",
                "price": {
                    "currency": "EUR",
                    "total": "1021.98",
                    "base": "635.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "1",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N"
                    },
                    {
                        "segmentId": "6",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N"
                    }
                ]
            },
            {
                "travelerId": "4",
                "fareOption": "STANDARD",
                "travelerType": "CHILD",
                "price": {
                    "currency": "EUR",
                    "total": "1021.98",
                    "base": "635.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "1",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N"
                    },
                    {
                        "segmentId": "6",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N"
                    }
                ]
            },
            {
                "travelerId": "5",
                "fareOption": "STANDARD",
                "travelerType": "HELD_INFANT",
                "associatedAdultId": "1",
                "price": {
                    "currency": "EUR",
                    "total": "139.31",
                    "base": "85.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "1",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N"
                    },
                    {
                        "segmentId": "6",
                        "cabin": "ECONOMY",
                        "fareBasis": "NNN7C2B4",
                        "brandedFare": "ELIGHT",
                        "class": "N"
                    }
                ]
            }
        ]
    },
}

OFFER_DETAILS_RESULT = {
    "price": 4649.23,
    "itineraries": [
        {
            "duration": 670,
            "segments": [
                {
                    "id": 1,
                    "departure": {
                        "airport": {
                            "iata": "FRA",
                            "name": "FRANKFURT INTL",
                            "city": "FRANKFURT",
                            "countryCode": "DE",
                            "country": "GERMANY",
                            "timezone": "+01:00"
                        },
                        "at": "2022-03-01T10:50:00"
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
                        "at": "2022-03-01T15:00:00"
                    },
                    "flightNumber": "AY5799",
                    "carrierCode": "AY",
                    "carrier": "FINNAIR",
                    "duration": 670,
                    "aircraft": "BOEING 787-8",
                    "cabin": "ECONOMY",
                    "classId": "N"
                }
            ]
        },
        {
            "duration": 570,
            "segments": [
                {
                    "id": 6,
                    "departure": {
                        "airport": {
                            "iata": "DFW",
                            "name": "DALLAS FT WORTH INTL",
                            "city": "DALLAS",
                            "countryCode": "US",
                            "country": "UNITED STATES OF AMERICA",
                            "timezone": "-06:00"
                        },
                        "at": "2022-03-03T16:00:00"
                    },
                    "arrival": {
                        "airport": {
                            "iata": "FRA",
                            "name": "FRANKFURT INTL",
                            "city": "FRANKFURT",
                            "countryCode": "DE",
                            "country": "GERMANY",
                            "timezone": "+01:00"
                        },
                        "at": "2022-03-04T08:30:00"
                    },
                    "flightNumber": "AY5800",
                    "carrierCode": "AY",
                    "carrier": "FINNAIR",
                    "duration": 570,
                    "aircraft": "BOEING 787-8",
                    "cabin": "ECONOMY",
                    "classId": "N"
                }
            ]
        }
    ]
}

OFFER_SEATMAP_RESULT = {
    "flightNumber": "AY5799",
    "classId": "N",
    "departureIata": "FRA",
    "arrivalIata": "DFW",
    "date": "2022-03-01T10:50:00",
    "amenities": {
        "power": {
            "isChargeable": False,
            "type": "USB-Port"
        },
        "seat": {
            "legSpace": "74 cm",
            "tilt": "Normal"
        },
        "wifi": {
            "isChargeable": True,
            "type": "Full"
        },
        "entertainment": [
            {
                "isChargeable": False,
                "type": "Audio & Video on demand"
            },
            {
                "isChargeable": False,
                "type": "IP-TV"
            }
        ],
        "food": {
            "isChargeable": False,
            "type": "Snacks"
        },
        "beverage": {
            "isChargeable": False,
            "type": "With and without alcohol"
        }
    },
    "decks": [
        {
            "exitRowsX": [
                10
            ],
            "wingsX": {
                "start": 0,
                "end": 9
            },
            "grid": [
                [
                    {
                        "type": "seat",
                        "number": "10A",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Chargeable seats"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "10B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Seat with bassinet facility",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "10C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Seat with bassinet facility",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "10D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "10E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "10H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "10J",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Chargeable seats"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "10K",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Chargeable seats"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "10L",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Chargeable seats"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "11A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "11B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "11C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "11D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "11E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "11H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "11J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "11K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "11L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "12A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "12B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "12C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "12D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "12E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "12H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "12J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "12K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "12L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "13A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "13B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "13C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "13D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "13E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "13H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "13J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "13K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "13L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "14A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "14B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "14C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "14D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "14E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "14H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "14J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "14K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "14L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "15A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "15B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "15C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "15D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "15E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "15H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "15J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "15K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "15L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "16A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "16B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "16C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "16D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "16E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "16H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "16J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "16K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "16L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "17A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "17B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "17C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "17D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "17E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "17H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "17J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "17K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "17L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "18A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "18B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "18C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "18D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "18E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "18H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "18J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "18K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "18L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "19A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "19C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "facility",
                        "name": "Lavatory"
                    },
                    None,
                    {
                        "type": "facility",
                        "name": "Lavatory"
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "19J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Medically OK to travel",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "19L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Chargeable seats",
                            "Overwing seat(s)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "20A",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Chargeable seats"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "20B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Exit row seat",
                            "Leg space seat",
                            "Chargeable seats",
                            "Seat not allowed for infant",
                            "Seat not allowed for medical",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "20C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Exit row seat",
                            "Leg space seat",
                            "Chargeable seats",
                            "Seat not allowed for infant",
                            "Seat not allowed for medical",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "20D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Seat with bassinet facility",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "20E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Seat with bassinet facility",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "20H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Leg space seat",
                            "Seat with bassinet facility",
                            "Chargeable seats",
                            "Bulkhead seat",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "20J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Exit row seat",
                            "Leg space seat",
                            "Chargeable seats",
                            "Seat not allowed for infant",
                            "Seat not allowed for medical",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "20K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Exit row seat",
                            "Leg space seat",
                            "Chargeable seats",
                            "Seat not allowed for infant",
                            "Seat not allowed for medical",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "20L",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Chargeable seats"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "21A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "21B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "21C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "Preferential seat",
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "21D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "21E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "21H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "21J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "21K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "21L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "22A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "22B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "22C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "22D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "22E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "22H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "22J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "22K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "22L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "23A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "23B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "23C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "23D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "23E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "23H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "23J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "23K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "23L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "24A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "24B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "24C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "24D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "24E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "24H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "24J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "24K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "24L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "25A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "25B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "25C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "25D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "25E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "25H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "25J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "25K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "25L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "26A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "26B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "26C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "26D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "26E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "26H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "26J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "26K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "26L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "27A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "27B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "27C",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Left side of aircraft"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "27D",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "27E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "27H",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Center section seat(s)"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "27J",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Medically OK to travel",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "27K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "27L",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "28A",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "28B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "28C",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "28D",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "28E",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Center section seat(s)"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "28H",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "28J",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "28K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "28L",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Window seat"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "29A",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Window seat"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "29B",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Left side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "29C",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "29D",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "29E",
                        "available": "OCCUPIED"
                    },
                    {
                        "type": "seat",
                        "number": "29H",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "29J",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "29K",
                        "available": "AVAILABLE",
                        "characteristics": [
                            "No facility seat (indifferent seat)",
                            "Right side of aircraft"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "29L",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Window seat"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "30A",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Window seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "30C",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "30D",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    {
                        "type": "seat",
                        "number": "30E",
                        "available": "OCCUPIED"
                    },
                    {
                        "type": "seat",
                        "number": "30H",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "30J",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "30L",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Window seat"
                        ]
                    }
                ],
                [
                    {
                        "type": "seat",
                        "number": "31A",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Window seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "31C",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "facility",
                        "name": "Galley"
                    },
                    None,
                    {
                        "type": "facility",
                        "name": "Galley"
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "31J",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Aisle seat"
                        ]
                    },
                    None,
                    {
                        "type": "seat",
                        "number": "31L",
                        "available": "OCCUPIED",
                        "characteristics": [
                            "Window seat"
                        ]
                    }
                ]
            ]
        }
    ]
}
