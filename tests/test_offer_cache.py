import unittest
from amadeus_connector.offer_cache import OfferCache
from amadeus_connector.errors import AmadeusNothingFound


class TestOfferCache(unittest.TestCase):

    def setUp(self):
        self.offer_cache = OfferCache(
            initial_state=INITIAL_STATE
        )

    def test_get_success(self):
        # get single offer
        self.assertDictEqual(self.offer_cache.get(
            [HASHES[0]]), {HASHES[0]: INITIAL_STATE[HASHES[0]]})
        self.assertDictEqual(self.offer_cache.get(
            [HASHES[2]]), {HASHES[2]: INITIAL_STATE[HASHES[2]]})
        # get multiple offers
        self.assertDictEqual(self.offer_cache.get(
            HASHES[2:5]), {h: INITIAL_STATE[h] for h in HASHES[2:5]})

    def test_get_nothing_found(self):
        # nothing found triggered by a single hash
        with self.assertRaises(AmadeusNothingFound):
            self.offer_cache.get(['abc'])
        # nothing found triggered by a two hashes
        with self.assertRaises(AmadeusNothingFound):
            self.offer_cache.get(['abc', 'def'])
        # wrong hash between right hashes
        with self.assertRaises(AmadeusNothingFound):
            self.offer_cache.get(HASHES[0:3] + ['abc'])

    def test_add_new(self):
        # add a single new offer
        new_hash = self.offer_cache.add([NEW_OFFER])[0]
        # check if now in cache available and correct
        self.assertDictEqual(self.offer_cache.get(
            [new_hash])[new_hash], NEW_OFFER)


if __name__ == '__main__':
    unittest.main()

INITIAL_STATE = {
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
    "e37de9039ad8a841c91ec24ba5d360635a0612c53fcdff256e13c7c675fc78562748138716ef788120c689c2307b033ef3af0b146d0e657febb47c23e3e8371e": {
        "type": "flight-offer",
        "id": "2",
        "source": "GDS",
        "instantTicketingRequired": False,
        "nonHomogeneous": False,
        "oneWay": False,
        "lastTicketingDate": "2022-02-20",
        "numberOfBookableSeats": 9,
        "itineraries": [
            {
                "duration": "PT13H50M",
                "segments": [
                    {
                        "departure": {
                            "iataCode": "FRA",
                            "terminal": "1",
                            "at": "2022-03-01T10:05:00"
                        },
                        "arrival": {
                            "iataCode": "YUL",
                            "at": "2022-03-01T12:05:00"
                        },
                        "carrierCode": "AC",
                        "number": "845",
                        "aircraft": {
                            "code": "77W"
                        },
                        "operating": {
                            "carrierCode": "AC"
                        },
                        "duration": "PT8H",
                        "id": "2",
                        "numberOfStops": 0,
                        "blacklistedInEU": False
                    },
                    {
                        "departure": {
                            "iataCode": "YUL",
                            "at": "2022-03-01T13:30:00"
                        },
                        "arrival": {
                            "iataCode": "DFW",
                            "terminal": "E",
                            "at": "2022-03-01T16:55:00"
                        },
                        "carrierCode": "AC",
                        "number": "7681",
                        "aircraft": {
                            "code": "E75"
                        },
                        "duration": "PT4H25M",
                        "id": "3",
                        "numberOfStops": 0,
                        "blacklistedInEU": False
                    }
                ]
            },
            {
                "duration": "PT9H50M",
                "segments": [
                    {
                        "departure": {
                            "iataCode": "DFW",
                            "terminal": "D",
                            "at": "2022-03-03T16:00:00"
                        },
                        "arrival": {
                            "iataCode": "FRA",
                            "terminal": "1",
                            "at": "2022-03-04T08:50:00"
                        },
                        "carrierCode": "LH",
                        "number": "439",
                        "aircraft": {
                            "code": "333"
                        },
                        "operating": {
                            "carrierCode": "LH"
                        },
                        "duration": "PT9H50M",
                        "id": "7",
                        "numberOfStops": 0,
                        "blacklistedInEU": False
                    }
                ]
            }
        ],
        "price": {
            "currency": "EUR",
            "total": "4709.23",
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
            "grandTotal": "4709.23"
        },
        "pricingOptions": {
            "fareType": [
                "PUBLISHED"
            ],
            "includedCheckedBagsOnly": False
        },
        "validatingAirlineCodes": [
            "AC"
        ],
        "travelerPricings": [
            {
                "travelerId": "1",
                "fareOption": "STANDARD",
                "travelerType": "ADULT",
                "price": {
                    "currency": "EUR",
                    "total": "1247.98",
                    "base": "846.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "2",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "class": "H",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    },
                    {
                        "segmentId": "3",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "BASIC",
                        "class": "H",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    },
                    {
                        "segmentId": "7",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "ECOLIGHT",
                        "class": "H",
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
                    "total": "1247.98",
                    "base": "846.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "2",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "class": "H",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    },
                    {
                        "segmentId": "3",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "BASIC",
                        "class": "H",
                        "includedCheckedBags": {
                            "quantity": 0
                        }
                    },
                    {
                        "segmentId": "7",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "ECOLIGHT",
                        "class": "H",
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
                    "total": "1036.98",
                    "base": "635.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "2",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "class": "H"
                    },
                    {
                        "segmentId": "3",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "BASIC",
                        "class": "H"
                    },
                    {
                        "segmentId": "7",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "ECOLIGHT",
                        "class": "H"
                    }
                ]
            },
            {
                "travelerId": "4",
                "fareOption": "STANDARD",
                "travelerType": "CHILD",
                "price": {
                    "currency": "EUR",
                    "total": "1036.98",
                    "base": "635.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "2",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "class": "H"
                    },
                    {
                        "segmentId": "3",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "BASIC",
                        "class": "H"
                    },
                    {
                        "segmentId": "7",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "ECOLIGHT",
                        "class": "H"
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
                        "segmentId": "2",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "class": "H"
                    },
                    {
                        "segmentId": "3",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "BASIC",
                        "class": "H"
                    },
                    {
                        "segmentId": "7",
                        "cabin": "ECONOMY",
                        "fareBasis": "HMPF2LGT",
                        "brandedFare": "ECOLIGHT",
                        "class": "H"
                    }
                ]
            }
        ]
    },
    "81399a2c34b5e448adc9c32b54c7ce780079d9aec52f01e77c797e905ce8160290395f86adab305d571b5da4308395a8ef615927c42ac735a7e8962366be20f8": {
        "type": "flight-offer",
        "id": "1",
        "itineraries": [
            {
                "segments": [
                    {
                        "departure": {
                            "iataCode": "FRA",
                            "at": "2022-03-01T00:00:00"
                        },
                        "arrival": {
                            "iataCode": "DFW"
                        },
                        "carrierCode": "LH",
                        "number": "438",
                        "id": "1"
                    }
                ]
            }
        ],
        "travelerPricings": [
            {
                "travelerId": "1",
                "travelerType": "ADULT",
                "fareDetailsBySegment": [
                    {
                        "segmentId": "1",
                        "class": "Y"
                    }
                ]
            }
        ]
    }
}

HASHES = [*INITIAL_STATE]

NEW_OFFER = {
    "type": "flight-offer",
    "id": "3",
    "source": "GDS",
    "instantTicketingRequired": False,
    "nonHomogeneous": False,
    "oneWay": False,
    "lastTicketingDate": "2022-02-20",
    "numberOfBookableSeats": 9,
    "itineraries": [
        {
            "duration": "PT13H50M",
            "segments": [
                {
                    "departure": {
                        "iataCode": "FRA",
                        "terminal": "1",
                        "at": "2022-03-01T10:05:00"
                    },
                    "arrival": {
                        "iataCode": "YUL",
                        "at": "2022-03-01T12:05:00"
                    },
                    "carrierCode": "UA",
                    "number": "8579",
                    "aircraft": {
                        "code": "77W"
                    },
                    "operating": {
                        "carrierCode": "AC"
                    },
                    "duration": "PT8H",
                    "id": "4",
                    "numberOfStops": 0,
                    "blacklistedInEU": False
                },
                {
                    "departure": {
                        "iataCode": "YUL",
                        "at": "2022-03-01T13:30:00"
                    },
                    "arrival": {
                        "iataCode": "DFW",
                        "terminal": "E",
                        "at": "2022-03-01T16:55:00"
                    },
                    "carrierCode": "UA",
                    "number": "8377",
                    "aircraft": {
                        "code": "E75"
                    },
                    "duration": "PT4H25M",
                    "id": "5",
                    "numberOfStops": 0,
                    "blacklistedInEU": False
                }
            ]
        },
        {
            "duration": "PT9H50M",
            "segments": [
                {
                    "departure": {
                        "iataCode": "DFW",
                        "terminal": "D",
                        "at": "2022-03-03T16:00:00"
                    },
                    "arrival": {
                        "iataCode": "FRA",
                        "terminal": "1",
                        "at": "2022-03-04T08:50:00"
                    },
                    "carrierCode": "LH",
                    "number": "439",
                    "aircraft": {
                        "code": "333"
                    },
                    "operating": {
                        "carrierCode": "LH"
                    },
                    "duration": "PT9H50M",
                    "id": "7",
                    "numberOfStops": 0,
                    "blacklistedInEU": False
                }
            ]
        }
    ],
    "price": {
        "currency": "EUR",
        "total": "4709.23",
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
        "grandTotal": "4709.23"
    },
    "pricingOptions": {
        "fareType": [
            "PUBLISHED"
        ],
        "includedCheckedBagsOnly": False
    },
    "validatingAirlineCodes": [
        "UA"
    ],
    "travelerPricings": [
        {
            "travelerId": "1",
            "fareOption": "STANDARD",
            "travelerType": "ADULT",
            "price": {
                "currency": "EUR",
                "total": "1247.98",
                "base": "846.00"
            },
            "fareDetailsBySegment": [
                {
                    "segmentId": "4",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "class": "H",
                    "includedCheckedBags": {
                        "quantity": 0
                    }
                },
                {
                    "segmentId": "5",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOBASIC",
                    "class": "H",
                    "includedCheckedBags": {
                        "quantity": 0
                    }
                },
                {
                    "segmentId": "7",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOLIGHT",
                    "class": "H",
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
                "total": "1247.98",
                "base": "846.00"
            },
            "fareDetailsBySegment": [
                {
                    "segmentId": "4",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "class": "H",
                    "includedCheckedBags": {
                        "quantity": 0
                    }
                },
                {
                    "segmentId": "5",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOBASIC",
                    "class": "H",
                    "includedCheckedBags": {
                        "quantity": 0
                    }
                },
                {
                    "segmentId": "7",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOLIGHT",
                    "class": "H",
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
                "total": "1036.98",
                "base": "635.00"
            },
            "fareDetailsBySegment": [
                {
                    "segmentId": "4",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "class": "H"
                },
                {
                    "segmentId": "5",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOBASIC",
                    "class": "H"
                },
                {
                    "segmentId": "7",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOLIGHT",
                    "class": "H"
                }
            ]
        },
        {
            "travelerId": "4",
            "fareOption": "STANDARD",
            "travelerType": "CHILD",
            "price": {
                "currency": "EUR",
                "total": "1036.98",
                "base": "635.00"
            },
            "fareDetailsBySegment": [
                {
                    "segmentId": "4",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "class": "H"
                },
                {
                    "segmentId": "5",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOBASIC",
                    "class": "H"
                },
                {
                    "segmentId": "7",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOLIGHT",
                    "class": "H"
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
                    "segmentId": "4",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "class": "H"
                },
                {
                    "segmentId": "5",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOBASIC",
                    "class": "H"
                },
                {
                    "segmentId": "7",
                    "cabin": "ECONOMY",
                    "fareBasis": "HMPF2LGT",
                    "brandedFare": "ECOLIGHT",
                    "class": "H"
                }
            ]
        }
    ]
}
