from unittest.mock import MagicMock
from amadeus import Client


class AmadeusResponse:
    def __init__(self, result):
        self.result = result


class AmadeusGetWrapper:
    def __init__(self, response):
        self.response = response

    def get(self):
        return self.response


class AmadeusMockClient(Client):
    def __init__(self):
        super().__init__(
            client_id='',
            client_secret='',
        )

        self.reference_data.locations.get = MagicMock(
            return_value=AmadeusResponse(AMADEUS_LOCATION_SEARCH)
        )

        self.reference_data.location = MagicMock(
            return_value=AmadeusGetWrapper(
                AmadeusResponse(AMADEUS_LOCATION_EXACT))
        )

        self.schedule.flights.get = MagicMock(
            return_value=AmadeusResponse(FLIGHT_SCHEDULE_LH438)
        )

        self.shopping.flight_offers_search.get = MagicMock(
            return_value=AmadeusResponse(AMADEUS_OFFER_SEARCH)
        )

        self.shopping.seatmaps.post = MagicMock(
            return_value=AmadeusResponse(AMADEUS_SEATMAP)
        )

        self.shopping.availability.flight_availabilities.post = MagicMock(
            return_value=AmadeusResponse(AMADEUS_AVAILABILITIES)
        )


AMADEUS_LOCATION_SEARCH = {
    "meta": {
        "count": 11,
        "links": {
            "self": "https://test.api.amadeus.com/v1/reference-data/locations?subType=AIRPORT&keyword=London&sort=analytics.travelers.score&view=FULL&page%5Boffset%5D=0&page%5Blimit%5D=10",
            "next": "https://test.api.amadeus.com/v1/reference-data/locations?subType=AIRPORT&keyword=London&sort=analytics.travelers.score&view=FULL&page%5Boffset%5D=10&page%5Blimit%5D=10",
            "last": "https://test.api.amadeus.com/v1/reference-data/locations?subType=AIRPORT&keyword=London&sort=analytics.travelers.score&view=FULL&page%5Boffset%5D=1&page%5Blimit%5D=10"
        }
    },
    "data": [
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "HEATHROW",
            "detailedName": "LONDON/GB:HEATHROW",
            "id": "ALHR",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ALHR",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "LHR",
            "geoCode": {
                "latitude": 51.47294,
                "longitude": -0.45061
            },
            "address": {
                "cityName": "LONDON",
                "cityCode": "LON",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            },
            "analytics": {
                "travelers": {
                    "score": 45
                }
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "GATWICK",
            "detailedName": "LONDON/GB:GATWICK",
            "id": "ALGW",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ALGW",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "LGW",
            "geoCode": {
                "latitude": 51.15609,
                "longitude": -0.17818
            },
            "address": {
                "cityName": "LONDON",
                "cityCode": "LON",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            },
            "analytics": {
                "travelers": {
                    "score": 27
                }
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "STANSTED",
            "detailedName": "LONDON/GB:STANSTED",
            "id": "ASTN",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ASTN",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "STN",
            "geoCode": {
                "latitude": 51.885,
                "longitude": 0.235
            },
            "address": {
                "cityName": "LONDON",
                "cityCode": "LON",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            },
            "analytics": {
                "travelers": {
                    "score": 15
                }
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "LUTON",
            "detailedName": "LONDON/GB:LUTON",
            "id": "ALTN",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ALTN",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "LTN",
            "geoCode": {
                "latitude": 51.87472,
                "longitude": -0.36833
            },
            "address": {
                "cityName": "LONDON",
                "cityCode": "LON",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            },
            "analytics": {
                "travelers": {
                    "score": 10
                }
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "CITY AIRPORT",
            "detailedName": "LONDON/GB:CITY AIRPORT",
            "id": "ALCY",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ALCY",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "LCY",
            "geoCode": {
                "latitude": 51.50528,
                "longitude": 0.05528
            },
            "address": {
                "cityName": "LONDON",
                "cityCode": "LON",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            },
            "analytics": {
                "travelers": {
                    "score": 4
                }
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "LONDON ASHFORD",
            "detailedName": "LYDD/GB:LONDON ASHFORD",
            "id": "ALYX",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ALYX",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "LYX",
            "geoCode": {
                "latitude": 50.95611,
                "longitude": 0.93917
            },
            "address": {
                "cityName": "LYDD",
                "cityCode": "LYX",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            },
            "analytics": {
                "travelers": {
                    "score": 2
                }
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "SOUTHEND",
            "detailedName": "LONDON/GB:SOUTHEND",
            "id": "ASEN",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ASEN",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "SEN",
            "geoCode": {
                "latitude": 51.57139,
                "longitude": 0.69556
            },
            "address": {
                "cityName": "LONDON",
                "cityCode": "LON",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            },
            "analytics": {
                "travelers": {
                    "score": 1
                }
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "BIGGIN HILL",
            "detailedName": "LONDON/GB:BIGGIN HILL",
            "id": "ABQH",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ABQH",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "+00:00",
            "iataCode": "BQH",
            "geoCode": {
                "latitude": 51.33083,
                "longitude": 0.0325
            },
            "address": {
                "cityName": "LONDON",
                "cityCode": "LON",
                "countryName": "UNITED KINGDOM",
                "countryCode": "GB",
                "regionCode": "EUROP"
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "AIRPORT",
            "detailedName": "GROTON NEW LONDON/CT/US:AIRPOR",
            "id": "AGON",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/AGON",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "-05:00",
            "iataCode": "GON",
            "geoCode": {
                "latitude": 41.3301,
                "longitude": -72.04452
            },
            "address": {
                "cityName": "GROTON NEW LONDON",
                "cityCode": "GON",
                "countryName": "UNITED STATES OF AMERICA",
                "countryCode": "US",
                "stateCode": "CT",
                "regionCode": "NAMER"
            }
        },
        {
            "type": "location",
            "subType": "AIRPORT",
            "name": "MAGEE FIELD",
            "detailedName": "LONDON/CORBIN/KY/US:MAGEE FIEL",
            "id": "ALOZ",
            "self": {
                "href": "https://test.api.amadeus.com/v1/reference-data/locations/ALOZ",
                "methods": [
                    "GET"
                ]
            },
            "timeZoneOffset": "-05:00",
            "iataCode": "LOZ",
            "geoCode": {
                "latitude": 37.08333,
                "longitude": -84.06667
            },
            "address": {
                "cityName": "LONDON/CORBIN",
                "cityCode": "LOZ",
                "countryName": "UNITED STATES OF AMERICA",
                "countryCode": "US",
                "stateCode": "KY",
                "regionCode": "NAMER"
            }
        }
    ]
}

AMADEUS_LOCATION_EXACT = {
    "meta": {
        "links": {
            "self": "https://test.api.amadeus.com/v1/reference-data/locations/ALHR"
        }
    },
    "data": {
        "type": "location",
        "subType": "AIRPORT",
        "name": "HEATHROW",
        "detailedName": "LONDON/GB:HEATHROW",
        "id": "ALHR",
        "self": {
            "href": "https://test.api.amadeus.com/v1/reference-data/locations/ALHR",
            "methods": [
                "GET"
            ]
        },
        "timeZoneOffset": "+00:00",
        "iataCode": "LHR",
        "geoCode": {
            "latitude": 51.47294,
            "longitude": -0.45061
        },
        "address": {
            "cityName": "LONDON",
            "cityCode": "LON",
            "countryName": "UNITED KINGDOM",
            "countryCode": "GB",
            "regionCode": "EUROP"
        },
        "analytics": {
            "travelers": {
                "score": 45
            }
        }
    }
}


FLIGHT_SCHEDULE_LH438 = {
    "meta": {
        "count": 1,
        "links": {
            "self": "https://test.api.amadeus.com/v2/schedule/flights?carrierCode=LH&flightNumber=438&scheduledDepartureDate=2022-03-01"
        }
    },
    "data": [
        {
            "type": "DatedFlight",
            "scheduledDepartureDate": "2022-03-01",
            "flightDesignator": {
                    "carrierCode": "LH",
                    "flightNumber": 438
            },
            "flightPoints": [
                {
                    "iataCode": "FRA",
                    "departure": {
                        "timings": [
                                {
                                    "qualifier": "STD",
                                    "value": "2022-03-01T09:55+01:00"
                                }
                        ]
                    }
                },
                {
                    "iataCode": "DFW",
                    "arrival": {
                        "timings": [
                                {
                                    "qualifier": "STA",
                                    "value": "2022-03-01T14:15-06:00"
                                }
                        ]
                    }
                }
            ],
            "segments": [
                {
                    "boardPointIataCode": "FRA",
                    "offPointIataCode": "DFW",
                    "scheduledSegmentDuration": "PT11H20M",
                    "partnership": {
                        "operatingFlight": {
                            "carrierCode": "UA",
                            "flightNumber": 8864
                        }
                    }
                }
            ],
            "legs": [
                {
                    "boardPointIataCode": "FRA",
                    "offPointIataCode": "DFW",
                    "aircraftEquipment": {
                        "aircraftType": "333"
                    },
                    "scheduledLegDuration": "PT11H20M"
                }
            ]
        }
    ]
}

AMADEUS_OFFER_SEARCH = {
    "meta": {
        "count": 5,
        "links": {
            "self": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=MUC&destinationLocationCode=DFW&departureDate=2022-03-01&returnDate=2022-03-08&adults=1&nonStop=False&currencyCode=EUR&max=5"
        }
    },
    "data": [
        {
            "type": "flight-offer",
            "id": "1",
            "source": "GDS",
            "instantTicketingRequired": False,
            "nonHomogeneous": False,
            "oneWay": False,
            "lastTicketingDate": "2022-02-22",
            "numberOfBookableSeats": 6,
            "itineraries": [
                {
                  "duration": "PT16H48M",
                  "segments": [
                      {
                          "departure": {
                              "iataCode": "MUC",
                              "terminal": "2",
                              "at": "2022-03-01T11:50:00"
                          },
                          "arrival": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T14:45:00"
                          },
                          "carrierCode": "AC",
                          "number": "837",
                          "aircraft": {
                              "code": "77W"
                          },
                          "operating": {
                              "carrierCode": "AC"
                          },
                          "duration": "PT8H55M",
                          "id": "1",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      },
                      {
                          "departure": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T19:05:00"
                          },
                          "arrival": {
                              "iataCode": "DFW",
                              "terminal": "E",
                              "at": "2022-03-01T21:38:00"
                          },
                          "carrierCode": "AC",
                          "number": "7615",
                          "aircraft": {
                              "code": "E75"
                          },
                          "duration": "PT3H33M",
                          "id": "2",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      }
                  ]
                },
                {
                    "duration": "PT11H49M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "DFW",
                                "terminal": "E",
                                "at": "2022-03-08T17:56:00"
                            },
                            "arrival": {
                                "iataCode": "ORD",
                                "terminal": "1",
                                "at": "2022-03-08T20:25:00"
                            },
                            "carrierCode": "LH",
                            "number": "7471",
                            "aircraft": {
                                "code": "319"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT2H29M",
                            "id": "11",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        },
                        {
                            "departure": {
                                "iataCode": "ORD",
                                "terminal": "1",
                                "at": "2022-03-08T21:25:00"
                            },
                            "arrival": {
                                "iataCode": "MUC",
                                "terminal": "2",
                                "at": "2022-03-09T12:45:00"
                            },
                            "carrierCode": "LH",
                            "number": "435",
                            "aircraft": {
                                "code": "359"
                            },
                            "operating": {
                                "carrierCode": "LH"
                            },
                            "duration": "PT8H20M",
                            "id": "12",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        }
                    ]
                }
            ],
            "price": {
                "currency": "EUR",
                "total": "781.55",
                "base": "386.00",
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
                "grandTotal": "781.55"
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
                        "total": "781.55",
                        "base": "386.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "1",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "2",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "BASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "11",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "12",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "ECOLIGHT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        }
                    ]
                }
            ]
        },
        {
            "type": "flight-offer",
            "id": "2",
            "source": "GDS",
            "instantTicketingRequired": False,
            "nonHomogeneous": False,
            "oneWay": False,
            "lastTicketingDate": "2022-02-22",
            "numberOfBookableSeats": 6,
            "itineraries": [
                {
                  "duration": "PT16H48M",
                  "segments": [
                      {
                          "departure": {
                              "iataCode": "MUC",
                              "terminal": "2",
                              "at": "2022-03-01T11:50:00"
                          },
                          "arrival": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T14:45:00"
                          },
                          "carrierCode": "UA",
                          "number": "8553",
                          "aircraft": {
                              "code": "77W"
                          },
                          "operating": {
                              "carrierCode": "AC"
                          },
                          "duration": "PT8H55M",
                          "id": "3",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      },
                      {
                          "departure": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T19:05:00"
                          },
                          "arrival": {
                              "iataCode": "DFW",
                              "terminal": "E",
                              "at": "2022-03-01T21:38:00"
                          },
                          "carrierCode": "UA",
                          "number": "8147",
                          "aircraft": {
                              "code": "E75"
                          },
                          "duration": "PT3H33M",
                          "id": "4",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      }
                  ]
                },
                {
                    "duration": "PT11H49M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "DFW",
                                "terminal": "E",
                                "at": "2022-03-08T17:56:00"
                            },
                            "arrival": {
                                "iataCode": "ORD",
                                "terminal": "1",
                                "at": "2022-03-08T20:25:00"
                            },
                            "carrierCode": "LH",
                            "number": "7471",
                            "aircraft": {
                                "code": "319"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT2H29M",
                            "id": "11",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        },
                        {
                            "departure": {
                                "iataCode": "ORD",
                                "terminal": "1",
                                "at": "2022-03-08T21:25:00"
                            },
                            "arrival": {
                                "iataCode": "MUC",
                                "terminal": "2",
                                "at": "2022-03-09T12:45:00"
                            },
                            "carrierCode": "LH",
                            "number": "435",
                            "aircraft": {
                                "code": "359"
                            },
                            "operating": {
                                "carrierCode": "LH"
                            },
                            "duration": "PT8H20M",
                            "id": "12",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        }
                    ]
                }
            ],
            "price": {
                "currency": "EUR",
                "total": "781.55",
                "base": "386.00",
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
                "grandTotal": "781.55"
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
                        "total": "781.55",
                        "base": "386.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "3",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "4",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "ECOBASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "11",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "12",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "ECOLIGHT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        }
                    ]
                }
            ]
        },
        {
            "type": "flight-offer",
            "id": "3",
            "source": "GDS",
            "instantTicketingRequired": False,
            "nonHomogeneous": False,
            "oneWay": False,
            "lastTicketingDate": "2022-02-22",
            "numberOfBookableSeats": 9,
            "itineraries": [
                {
                  "duration": "PT16H48M",
                  "segments": [
                      {
                          "departure": {
                              "iataCode": "MUC",
                              "terminal": "2",
                              "at": "2022-03-01T11:50:00"
                          },
                          "arrival": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T14:45:00"
                          },
                          "carrierCode": "AC",
                          "number": "837",
                          "aircraft": {
                              "code": "77W"
                          },
                          "operating": {
                              "carrierCode": "AC"
                          },
                          "duration": "PT8H55M",
                          "id": "1",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      },
                      {
                          "departure": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T19:05:00"
                          },
                          "arrival": {
                              "iataCode": "DFW",
                              "terminal": "E",
                              "at": "2022-03-01T21:38:00"
                          },
                          "carrierCode": "AC",
                          "number": "7615",
                          "aircraft": {
                              "code": "E75"
                          },
                          "duration": "PT3H33M",
                          "id": "2",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      }
                  ]
                },
                {
                    "duration": "PT12H11M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "DFW",
                                "terminal": "E",
                                "at": "2022-03-08T12:29:00"
                            },
                            "arrival": {
                                "iataCode": "IAD",
                                "at": "2022-03-08T16:11:00"
                            },
                            "carrierCode": "UA",
                            "number": "2454",
                            "aircraft": {
                                "code": "738"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT2H42M",
                            "id": "5",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        },
                        {
                            "departure": {
                                "iataCode": "IAD",
                                "at": "2022-03-08T17:30:00"
                            },
                            "arrival": {
                                "iataCode": "MUC",
                                "terminal": "2",
                                "at": "2022-03-09T07:40:00"
                            },
                            "carrierCode": "UA",
                            "number": "106",
                            "aircraft": {
                                "code": "777"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT8H10M",
                            "id": "6",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        }
                    ]
                }
            ],
            "price": {
                "currency": "EUR",
                "total": "781.55",
                "base": "386.00",
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
                "grandTotal": "781.55"
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
                        "total": "781.55",
                        "base": "386.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "1",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "2",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "BASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "5",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "6",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "ECOBASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        }
                    ]
                }
            ]
        },
        {
            "type": "flight-offer",
            "id": "4",
            "source": "GDS",
            "instantTicketingRequired": False,
            "nonHomogeneous": False,
            "oneWay": False,
            "lastTicketingDate": "2022-02-22",
            "numberOfBookableSeats": 9,
            "itineraries": [
                {
                  "duration": "PT16H48M",
                  "segments": [
                      {
                          "departure": {
                              "iataCode": "MUC",
                              "terminal": "2",
                              "at": "2022-03-01T11:50:00"
                          },
                          "arrival": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T14:45:00"
                          },
                          "carrierCode": "AC",
                          "number": "837",
                          "aircraft": {
                              "code": "77W"
                          },
                          "operating": {
                              "carrierCode": "AC"
                          },
                          "duration": "PT8H55M",
                          "id": "1",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      },
                      {
                          "departure": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T19:05:00"
                          },
                          "arrival": {
                              "iataCode": "DFW",
                              "terminal": "E",
                              "at": "2022-03-01T21:38:00"
                          },
                          "carrierCode": "AC",
                          "number": "7615",
                          "aircraft": {
                              "code": "E75"
                          },
                          "duration": "PT3H33M",
                          "id": "2",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      }
                  ]
                },
                {
                    "duration": "PT12H34M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "DFW",
                                "terminal": "E",
                                "at": "2022-03-08T14:01:00"
                            },
                            "arrival": {
                                "iataCode": "ORD",
                                "terminal": "1",
                                "at": "2022-03-08T16:25:00"
                            },
                            "carrierCode": "UA",
                            "number": "1937",
                            "aircraft": {
                                "code": "319"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT2H24M",
                            "id": "7",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        },
                        {
                            "departure": {
                                "iataCode": "ORD",
                                "terminal": "1",
                                "at": "2022-03-08T18:05:00"
                            },
                            "arrival": {
                                "iataCode": "MUC",
                                "terminal": "2",
                                "at": "2022-03-09T09:35:00"
                            },
                            "carrierCode": "UA",
                            "number": "953",
                            "aircraft": {
                                "code": "788"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT8H30M",
                            "id": "8",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        }
                    ]
                }
            ],
            "price": {
                "currency": "EUR",
                "total": "781.55",
                "base": "386.00",
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
                "grandTotal": "781.55"
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
                        "total": "781.55",
                        "base": "386.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "1",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "2",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "BASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "7",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "8",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "ECOBASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        }
                    ]
                }
            ]
        },
        {
            "type": "flight-offer",
            "id": "5",
            "source": "GDS",
            "instantTicketingRequired": False,
            "nonHomogeneous": False,
            "oneWay": False,
            "lastTicketingDate": "2022-02-22",
            "numberOfBookableSeats": 9,
            "itineraries": [
                {
                  "duration": "PT16H48M",
                  "segments": [
                      {
                          "departure": {
                              "iataCode": "MUC",
                              "terminal": "2",
                              "at": "2022-03-01T11:50:00"
                          },
                          "arrival": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T14:45:00"
                          },
                          "carrierCode": "AC",
                          "number": "837",
                          "aircraft": {
                              "code": "77W"
                          },
                          "operating": {
                              "carrierCode": "AC"
                          },
                          "duration": "PT8H55M",
                          "id": "1",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      },
                      {
                          "departure": {
                              "iataCode": "YYZ",
                              "terminal": "1",
                              "at": "2022-03-01T19:05:00"
                          },
                          "arrival": {
                              "iataCode": "DFW",
                              "terminal": "E",
                              "at": "2022-03-01T21:38:00"
                          },
                          "carrierCode": "AC",
                          "number": "7615",
                          "aircraft": {
                              "code": "E75"
                          },
                          "duration": "PT3H33M",
                          "id": "2",
                          "numberOfStops": 0,
                          "blacklistedInEU": False
                      }
                  ]
                },
                {
                    "duration": "PT13H35M",
                    "segments": [
                        {
                            "departure": {
                                "iataCode": "DFW",
                                "terminal": "E",
                                "at": "2022-03-08T10:45:00"
                            },
                            "arrival": {
                                "iataCode": "EWR",
                                "terminal": "C",
                                "at": "2022-03-08T15:06:00"
                            },
                            "carrierCode": "UA",
                            "number": "1003",
                            "aircraft": {
                                "code": "320"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT3H21M",
                            "id": "9",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        },
                        {
                            "departure": {
                                "iataCode": "EWR",
                                "terminal": "C",
                                "at": "2022-03-08T17:20:00"
                            },
                            "arrival": {
                                "iataCode": "MUC",
                                "terminal": "2",
                                "at": "2022-03-09T07:20:00"
                            },
                            "carrierCode": "UA",
                            "number": "30",
                            "aircraft": {
                                "code": "763"
                            },
                            "operating": {
                                "carrierCode": "UA"
                            },
                            "duration": "PT8H",
                            "id": "10",
                            "numberOfStops": 0,
                            "blacklistedInEU": False
                        }
                    ]
                }
            ],
            "price": {
                "currency": "EUR",
                "total": "781.55",
                "base": "386.00",
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
                "grandTotal": "781.55"
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
                        "total": "781.55",
                        "base": "386.00"
                    },
                    "fareDetailsBySegment": [
                        {
                            "segmentId": "1",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "2",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "BASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "9",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        },
                        {
                            "segmentId": "10",
                            "cabin": "ECONOMY",
                            "fareBasis": "TMPF8LGT",
                            "brandedFare": "ECOBASIC",
                            "class": "T",
                            "includedCheckedBags": {
                                "quantity": 0
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "dictionaries": {
        "locations": {
            "ORD": {
                "cityCode": "CHI",
                "countryCode": "US"
            },
            "EWR": {
                "cityCode": "NYC",
                "countryCode": "US"
            },
            "DFW": {
                "cityCode": "DFW",
                "countryCode": "US"
            },
            "MUC": {
                "cityCode": "MUC",
                "countryCode": "DE"
            },
            "YYZ": {
                "cityCode": "YTO",
                "countryCode": "CA"
            },
            "IAD": {
                "cityCode": "WAS",
                "countryCode": "US"
            }
        },
        "aircraft": {
            "319": "AIRBUS A319",
            "320": "AIRBUS A320",
            "359": "AIRBUS A350-900",
            "738": "BOEING 737-800",
            "763": "BOEING 767-300/300ER",
            "777": "BOEING 777-200/300",
            "788": "BOEING 787-8",
            "E75": "EMBRAER 175",
            "77W": "BOEING 777-300ER"
        },
        "currencies": {
            "EUR": "EURO"
        },
        "carriers": {
            "AC": "AIR CANADA",
            "LH": "LUFTHANSA",
            "UA": "UNITED AIRLINES"
        }
    }
}

AMADEUS_SEATMAP = {
    "meta": {
        "count": 2
    },
    "data": [
        {
            "id": "1",
            "type": "seatmap",
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
            "operating": {
                "carrierCode": "AA"
            },
            "aircraft": {
                "code": "788"
            },
            "class": "N",
            "flightOfferId": "1",
            "segmentId": "1",
            "decks": [
                {
                    "deckType": "MAIN",
                    "deckConfiguration": {
                        "width": 11,
                        "length": 22,
                        "startSeatRow": 10,
                        "endSeatRow": 31,
                        "startWingsX": 0,
                        "endWingsX": 9,
                        "startWingsRow": 10,
                        "endWingsRow": 19,
                        "exitRowsX": [
                            10
                        ]
                    },
                    "facilities": [
                        {
                            "code": "LA",
                            "column": "D",
                            "row": "19",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 9,
                                "y": 4
                            }
                        },
                        {
                            "code": "LA",
                            "column": "H",
                            "row": "19",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 9,
                                "y": 6
                            }
                        },
                        {
                            "code": "GN",
                            "column": "D",
                            "row": "31",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 21,
                                "y": 4
                            }
                        },
                        {
                            "code": "GN",
                            "column": "H",
                            "row": "31",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 21,
                                "y": 6
                            }
                        }
                    ],
                    "seats": [
                        {
                            "cabin": "ECONOMY",
                            "number": "10A",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10B",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10C",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "K",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "K",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "K",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10J",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10K",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10L",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11A",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11B",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11C",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11J",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11K",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11L",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20A",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20B",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20C",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20D",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20E",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20H",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20J",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20K",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20L",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21C",
                            "characteristicsCodes": [
                                "O",
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28C",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28D",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28H",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28J",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29C",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29D",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29E",
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29H",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29J",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30C",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30D",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30E",
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30H",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30J",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31C",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31J",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 10
                            }
                        }
                    ]
                }
            ],
            "aircraftCabinAmenities": {
                "power": {
                    "isChargeable": False,
                    "powerType": "USB_PORT"
                },
                "seat": {
                    "legSpace": 29,
                    "spaceUnit": "INCHES",
                    "tilt": "NORMAL",
                    "medias": [
                        {
                            "title": "Comfortable Seats",
                            "href": "https://pdt.content.amadeus.com/AncillaryServicesMedia/14223418_395.jpg",
                            "description": {
                                "text": "Settle in with comfortable seats and an ecoTHREAD blanket made from 100% recycled plastic bottles.",
                                "lang": "EN"
                            },
                            "mediaType": "image"
                        },
                        {
                            "title": "Stay Connected",
                            "href": "https://pdt.content.amadeus.com/AncillaryServicesMedia/71344149_DFL.jpg",
                            "description": {
                                "text": "Stay connected next time you fly. Choose from our great value Wi-Fi plans.",
                                "lang": "EN"
                            },
                            "mediaType": "image"
                        },
                        {
                            "title": "Be Curious",
                            "href": "https://pdt.content.amadeus.com/AncillaryServicesMedia/42266150_401.jpg",
                            "description": {
                                "text": "With special seat,meals, toys, and dedicated children's ice channels, we encourage curious minds and inspire tomorrow's explorers.",
                                "lang": "EN"
                            },
                            "mediaType": "image"
                        }
                    ]
                },
                "wifi": {
                    "isChargeable": True,
                    "wifiCoverage": "FULL"
                },
                "entertainment": [
                    {
                        "isChargeable": False,
                        "entertainmentType": "AUDIO_VIDEO_ON_DEMAND"
                    },
                    {
                        "isChargeable": False,
                        "entertainmentType": "IP_TV"
                    }
                ],
                "food": {
                    "isChargeable": False,
                    "foodType": "SNACK"
                },
                "beverage": {
                    "isChargeable": False,
                    "beverageType": "ALCOHOLIC_AND_NON_ALCOHOLIC"
                }
            },
            "availableSeatsCounters": [
                {
                    "travelerId": "1",
                    "value": 157
                },
                {
                    "travelerId": "2",
                    "value": 157
                },
                {
                    "travelerId": "3",
                    "value": 157
                },
                {
                    "travelerId": "4",
                    "value": 157
                },
                {
                    "travelerId": "5",
                    "value": 157
                }
            ]
        },
        {
            "id": "2",
            "type": "seatmap",
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
            "operating": {
                "carrierCode": "AA"
            },
            "aircraft": {
                "code": "788"
            },
            "class": "N",
            "flightOfferId": "1",
            "segmentId": "6",
            "decks": [
                {
                    "deckType": "MAIN",
                    "deckConfiguration": {
                        "width": 11,
                        "length": 22,
                        "startSeatRow": 10,
                        "endSeatRow": 31,
                        "startWingsX": 0,
                        "endWingsX": 9,
                        "startWingsRow": 10,
                        "endWingsRow": 19,
                        "exitRowsX": [
                            10
                        ]
                    },
                    "facilities": [
                        {
                            "code": "LA",
                            "column": "D",
                            "row": "19",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 9,
                                "y": 4
                            }
                        },
                        {
                            "code": "LA",
                            "column": "H",
                            "row": "19",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 9,
                                "y": 6
                            }
                        },
                        {
                            "code": "GN",
                            "column": "D",
                            "row": "31",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 21,
                                "y": 4
                            }
                        },
                        {
                            "code": "GN",
                            "column": "H",
                            "row": "31",
                            "position": "SEAT",
                            "coordinates": {
                                "x": 21,
                                "y": 6
                            }
                        }
                    ],
                    "seats": [
                        {
                            "cabin": "ECONOMY",
                            "number": "10A",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10B",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10C",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "K",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "K",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "K",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10J",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10K",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "10L",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 0,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11A",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11B",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11C",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11J",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11K",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "11L",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 1,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12C",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "12L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 2,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "13L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 3,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "14L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 4,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "15L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 5,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "16L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 6,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "17L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 7,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18B",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18D",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18E",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18H",
                            "characteristicsCodes": [
                                "L",
                                "CH",
                                "MA",
                                "OW",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18K",
                            "characteristicsCodes": [
                                "X",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "18L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 8,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19A",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19C",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19J",
                            "characteristicsCodes": [
                                "CH",
                                "MA",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "19L",
                            "characteristicsCodes": [
                                "CH",
                                "OW",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 9,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20A",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20B",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20C",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20D",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20E",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20H",
                            "characteristicsCodes": [
                                "L",
                                "B",
                                "CH",
                                "K",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20J",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20K",
                            "characteristicsCodes": [
                                "E",
                                "L",
                                "CH",
                                "1A",
                                "1B",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "20L",
                            "characteristicsCodes": [
                                "CH"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 10,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21C",
                            "characteristicsCodes": [
                                "O",
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "21L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 11,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "22L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 12,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "23L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 13,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "24L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 14,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "25L",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 15,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26A",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "26L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 16,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "27L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 17,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28D",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28E",
                            "characteristicsCodes": [
                                "X",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28H",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "CC"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28J",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "28L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 18,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29B",
                            "characteristicsCodes": [
                                "X",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 1
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29C",
                            "characteristicsCodes": [
                                "X",
                                "MA",
                                "LS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29D",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29E",
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29H",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29J",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29K",
                            "characteristicsCodes": [
                                "X",
                                "RS"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "AVAILABLE"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 9
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "29L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 19,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30C",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30D",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 4
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30E",
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 5
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30H",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 6
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30J",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "30L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 20,
                                "y": 10
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31A",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 0
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31C",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 2
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31J",
                            "characteristicsCodes": [
                                "A"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 8
                            }
                        },
                        {
                            "cabin": "ECONOMY",
                            "number": "31L",
                            "characteristicsCodes": [
                                "W"
                            ],
                            "travelerPricing": [
                                {
                                    "travelerId": "1",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "2",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "3",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "4",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                },
                                {
                                    "travelerId": "5",
                                    "seatAvailabilityStatus": "OCCUPIED"
                                }
                            ],
                            "coordinates": {
                                "x": 21,
                                "y": 10
                            }
                        }
                    ]
                }
            ],
            "aircraftCabinAmenities": {
                "power": {
                    "isChargeable": False,
                    "powerType": "USB_PORT"
                },
                "seat": {
                    "legSpace": 29,
                    "spaceUnit": "INCHES",
                    "tilt": "NORMAL",
                    "medias": [
                        {
                            "title": "Comfortable Seats",
                            "href": "https://pdt.content.amadeus.com/AncillaryServicesMedia/14223418_395.jpg",
                            "description": {
                                "text": "Settle in with comfortable seats and an ecoTHREAD blanket made from 100% recycled plastic bottles.",
                                "lang": "EN"
                            },
                            "mediaType": "image"
                        },
                        {
                            "title": "Stay Connected",
                            "href": "https://pdt.content.amadeus.com/AncillaryServicesMedia/71344149_DFL.jpg",
                            "description": {
                                "text": "Stay connected next time you fly. Choose from our great value Wi-Fi plans.",
                                "lang": "EN"
                            },
                            "mediaType": "image"
                        },
                        {
                            "title": "Be Curious",
                            "href": "https://pdt.content.amadeus.com/AncillaryServicesMedia/42266150_401.jpg",
                            "description": {
                                "text": "With special seat,meals, toys, and dedicated children's ice channels, we encourage curious minds and inspire tomorrow's explorers.",
                                "lang": "EN"
                            },
                            "mediaType": "image"
                        }
                    ]
                },
                "wifi": {
                    "isChargeable": True,
                    "wifiCoverage": "FULL"
                },
                "entertainment": [
                    {
                        "isChargeable": False,
                        "entertainmentType": "AUDIO_VIDEO_ON_DEMAND"
                    },
                    {
                        "isChargeable": False,
                        "entertainmentType": "IP_TV"
                    }
                ],
                "food": {
                    "isChargeable": False,
                    "foodType": "SNACK"
                },
                "beverage": {
                    "isChargeable": False,
                    "beverageType": "ALCOHOLIC_AND_NON_ALCOHOLIC"
                }
            },
            "availableSeatsCounters": [
                {
                    "travelerId": "1",
                    "value": 157
                },
                {
                    "travelerId": "2",
                    "value": 157
                },
                {
                    "travelerId": "3",
                    "value": 157
                },
                {
                    "travelerId": "4",
                    "value": 157
                },
                {
                    "travelerId": "5",
                    "value": 157
                }
            ]
        }
    ],
    "dictionaries": {
        "locations": {
            "DFW": {
                "cityCode": "DFW",
                "countryCode": "US"
            },
            "FRA": {
                "cityCode": "FRA",
                "countryCode": "DE"
            }
        },
        "facilities": {
            "LA": "Lavatory",
            "GN": "Galley"
        },
        "seatCharacteristics": {
            "CC": "Center section seat(s)",
            "RS": "Right side of aircraft",
            "A": "Aisle seat",
            "B": "Seat with bassinet facility",
            "CH": "Chargeable seats",
            "E": "Exit row seat",
            "LS": "Left side of aircraft",
            "OW": "Overwing seat(s)",
            "K": "Bulkhead seat",
            "L": "Leg space seat",
            "O": "Preferential seat",
            "1A": "Seat not allowed for infant",
            "1B": "Seat not allowed for medical",
            "MA": "Medically OK to travel",
            "W": "Window seat",
            "X": "No facility seat (indifferent seat)"
        }
    }
}

AMADEUS_AVAILABILITIES = {
  "meta": {
    "count": 45
  },
  "data": [
    {
      "type": "flight-availability",
      "id": "1",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H56M",
      "segments": [
        {
          "id": "50",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T03:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T05:00:00"
          },
          "carrierCode": "7X",
          "number": "1117",
          "aircraft": {
            "code": "744"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "51",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LGA",
            "terminal": "B",
            "at": "2022-03-01T07:47:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "0",
            "at": "2022-03-01T10:56:00"
          },
          "carrierCode": "B6",
          "number": "4192",
          "aircraft": {
            "code": "321"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "P"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "2",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H36M",
      "segments": [
        {
          "id": "66",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T03:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T05:00:00"
          },
          "carrierCode": "7X",
          "number": "1117",
          "aircraft": {
            "code": "744"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "67",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "JFK",
            "terminal": "8",
            "at": "2022-03-01T08:21:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "0",
            "at": "2022-03-01T11:36:00"
          },
          "carrierCode": "AT",
          "number": "5065",
          "aircraft": {
            "code": "738"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Y"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "3",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT16H",
      "segments": [
        {
          "id": "74",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T03:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T05:00:00"
          },
          "carrierCode": "7X",
          "number": "1117",
          "aircraft": {
            "code": "744"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "75",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LGA",
            "terminal": "0",
            "at": "2022-03-01T09:10:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T12:00:00"
          },
          "carrierCode": "DL",
          "number": "561",
          "aircraft": {
            "code": "223"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "4",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H40M",
      "segments": [
        {
          "id": "4",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T03:20:00"
          },
          "arrival": {
            "iataCode": "LAX",
            "terminal": "1",
            "at": "2022-03-01T04:00:00"
          },
          "carrierCode": "6X",
          "number": "456",
          "aircraft": {
            "code": "320"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        },
        {
          "id": "5",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LAX",
            "at": "2022-03-01T07:00:00"
          },
          "arrival": {
            "iataCode": "DAL",
            "at": "2022-03-01T10:00:00"
          },
          "carrierCode": "6X",
          "number": "3693",
          "aircraft": {
            "code": "767"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 8,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "5",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H40M",
      "segments": [
        {
          "id": "10",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T03:20:00"
          },
          "arrival": {
            "iataCode": "LAX",
            "at": "2022-03-01T04:00:00"
          },
          "carrierCode": "6X",
          "number": "123",
          "aircraft": {
            "code": "772"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        },
        {
          "id": "11",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LAX",
            "at": "2022-03-01T07:00:00"
          },
          "arrival": {
            "iataCode": "DAL",
            "at": "2022-03-01T10:00:00"
          },
          "carrierCode": "6X",
          "number": "3693",
          "aircraft": {
            "code": "767"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 8,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "6",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H",
      "segments": [
        {
          "id": "22",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T04:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T06:00:00"
          },
          "carrierCode": "6X",
          "number": "3758",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "23",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "JFK",
            "terminal": "1",
            "at": "2022-03-01T08:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "2",
            "at": "2022-03-01T11:00:00"
          },
          "carrierCode": "6X",
          "number": "632",
          "aircraft": {
            "code": "767"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 8,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 5,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "7",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H36M",
      "segments": [
        {
          "id": "42",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T04:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T06:00:00"
          },
          "carrierCode": "6X",
          "number": "3758",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "43",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "JFK",
            "terminal": "8",
            "at": "2022-03-01T08:21:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "0",
            "at": "2022-03-01T11:36:00"
          },
          "carrierCode": "AT",
          "number": "5065",
          "aircraft": {
            "code": "738"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "P"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "8",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H",
      "segments": [
        {
          "id": "52",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T04:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T06:00:00"
          },
          "carrierCode": "6X",
          "number": "3758",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "53",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LGA",
            "terminal": "0",
            "at": "2022-03-01T09:10:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T12:00:00"
          },
          "carrierCode": "DL",
          "number": "561",
          "aircraft": {
            "code": "223"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "9",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H10M",
      "segments": [
        {
          "id": "54",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T04:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T06:00:00"
          },
          "carrierCode": "6X",
          "number": "3758",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "55",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "JFK",
            "at": "2022-03-01T09:00:00"
          },
          "arrival": {
            "iataCode": "DAL",
            "at": "2022-03-01T12:10:00"
          },
          "carrierCode": "6X",
          "number": "3671",
          "aircraft": {
            "code": "767"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 8,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "10",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H14M",
      "segments": [
        {
          "id": "58",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T04:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "at": "2022-03-01T06:00:00"
          },
          "carrierCode": "6X",
          "number": "3758",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            }
          ]
        },
        {
          "id": "59",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LGA",
            "terminal": "B",
            "at": "2022-03-01T09:00:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "0",
            "at": "2022-03-01T12:14:00"
          },
          "carrierCode": "B6",
          "number": "4116",
          "aircraft": {
            "code": "321"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "P"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "11",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H25M",
      "segments": [
        {
          "id": "38",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T07:00:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "terminal": "2",
            "at": "2022-03-01T07:45:00"
          },
          "carrierCode": "LH",
          "number": "924",
          "aircraft": {
            "code": "32Q"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "39",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "3",
            "at": "2022-03-01T09:55:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T14:25:00"
          },
          "carrierCode": "AY",
          "number": "4177",
          "aircraft": {
            "code": "77W"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 5,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "12",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H45M",
      "segments": [
        {
          "id": "48",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T07:00:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "terminal": "2",
            "at": "2022-03-01T07:45:00"
          },
          "carrierCode": "LH",
          "number": "924",
          "aircraft": {
            "code": "32Q"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "49",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LGW",
            "terminal": "N",
            "at": "2022-03-01T10:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "B",
            "at": "2022-03-01T14:45:00"
          },
          "carrierCode": "6X",
          "number": "2193",
          "aircraft": {
            "code": "772"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "13",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H25M",
      "segments": [
        {
          "id": "40",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:35:00"
          },
          "arrival": {
            "iataCode": "CDG",
            "at": "2022-03-01T08:35:00"
          },
          "carrierCode": "6X",
          "number": "7073",
          "aircraft": {
            "code": "738"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            }
          ]
        },
        {
          "id": "41",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "CDG",
            "terminal": "2A",
            "at": "2022-03-01T11:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T15:00:00"
          },
          "carrierCode": "IB",
          "number": "4191",
          "aircraft": {
            "code": "789"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "14",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT16H",
      "segments": [
        {
          "id": "76",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:35:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T08:35:00"
          },
          "carrierCode": "6X",
          "number": "3803",
          "aircraft": {
            "code": "738"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            }
          ]
        },
        {
          "id": "77",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "AY",
          "number": "5493",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 3,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "15",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT16H",
      "segments": [
        {
          "id": "78",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:35:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T08:35:00"
          },
          "carrierCode": "6X",
          "number": "7041",
          "aircraft": {
            "code": "738"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            }
          ]
        },
        {
          "id": "79",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "AY",
          "number": "5493",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 3,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "16",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT16H",
      "segments": [
        {
          "id": "80",
          "numberOfStops": 1,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:35:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T09:30:00"
          },
          "carrierCode": "6X",
          "number": "7074",
          "aircraft": {
            "code": "738"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            }
          ]
        },
        {
          "id": "81",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "IB",
          "number": "7388",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "17",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT16H",
      "segments": [
        {
          "id": "82",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:35:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T08:35:00"
          },
          "carrierCode": "6X",
          "number": "3803",
          "aircraft": {
            "code": "738"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            }
          ]
        },
        {
          "id": "83",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "IB",
          "number": "7388",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "18",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT16H",
      "segments": [
        {
          "id": "84",
          "numberOfStops": 1,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:35:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T09:30:00"
          },
          "carrierCode": "6X",
          "number": "7073",
          "aircraft": {
            "code": "738"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            }
          ]
        },
        {
          "id": "85",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "IB",
          "number": "7388",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "19",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT16H",
      "segments": [
        {
          "id": "86",
          "numberOfStops": 1,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:35:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T09:30:00"
          },
          "carrierCode": "6X",
          "number": "7060",
          "aircraft": {
            "code": "738"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            }
          ]
        },
        {
          "id": "87",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "IB",
          "number": "7388",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "20",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H50M",
      "segments": [
        {
          "id": "70",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:45:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T08:35:00"
          },
          "carrierCode": "7X",
          "number": "3601",
          "aircraft": {
            "code": "319"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        },
        {
          "id": "71",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "IB",
          "number": "7388",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "21",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H50M",
      "segments": [
        {
          "id": "72",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T07:45:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "at": "2022-03-01T08:35:00"
          },
          "carrierCode": "7X",
          "number": "3601",
          "aircraft": {
            "code": "319"
          },
          "operating": {
            "carrierCode": "6X"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        },
        {
          "id": "73",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "AY",
          "number": "5493",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 3,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "22",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H35M",
      "segments": [
        {
          "id": "64",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T08:00:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "terminal": "2",
            "at": "2022-03-01T08:45:00"
          },
          "carrierCode": "LH",
          "number": "900",
          "aircraft": {
            "code": "32Q"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "65",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "AY",
          "number": "5493",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 3,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "23",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H40M",
      "segments": [
        {
          "id": "12",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T08:20:00"
          },
          "arrival": {
            "iataCode": "CDG",
            "at": "2022-03-01T09:35:00"
          },
          "carrierCode": "6X",
          "number": "1193",
          "aircraft": {
            "code": "733"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            }
          ]
        },
        {
          "id": "13",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "CDG",
            "terminal": "2A",
            "at": "2022-03-01T11:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T15:00:00"
          },
          "carrierCode": "AY",
          "number": "5777",
          "aircraft": {
            "code": "789"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "24",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H40M",
      "segments": [
        {
          "id": "14",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T08:20:00"
          },
          "arrival": {
            "iataCode": "CDG",
            "terminal": "2B",
            "at": "2022-03-01T09:35:00"
          },
          "carrierCode": "SQ",
          "number": "2074",
          "aircraft": {
            "code": "32A"
          },
          "operating": {
            "carrierCode": "LH"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "15",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "CDG",
            "terminal": "2A",
            "at": "2022-03-01T11:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T15:00:00"
          },
          "carrierCode": "IB",
          "number": "4191",
          "aircraft": {
            "code": "789"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "25",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H35M",
      "segments": [
        {
          "id": "6",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T08:25:00"
          },
          "arrival": {
            "iataCode": "CDG",
            "at": "2022-03-01T09:45:00"
          },
          "carrierCode": "7S",
          "number": "104",
          "aircraft": {
            "code": "320"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            }
          ]
        },
        {
          "id": "7",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "CDG",
            "terminal": "2A",
            "at": "2022-03-01T11:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T15:00:00"
          },
          "carrierCode": "AY",
          "number": "5777",
          "aircraft": {
            "code": "789"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "26",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H12M",
      "segments": [
        {
          "id": "32",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T08:35:00"
          },
          "arrival": {
            "iataCode": "ORD",
            "terminal": "5",
            "at": "2022-03-01T10:55:00"
          },
          "carrierCode": "LH",
          "number": "9152",
          "aircraft": {
            "code": "787"
          },
          "operating": {
            "carrierCode": "UA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            }
          ]
        },
        {
          "id": "33",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "ORD",
            "terminal": "1",
            "at": "2022-03-01T13:20:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T15:47:00"
          },
          "carrierCode": "UA",
          "number": "2211",
          "aircraft": {
            "code": "319"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "27",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H40M",
      "segments": [
        {
          "id": "44",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T09:00:00"
          },
          "arrival": {
            "iataCode": "AMS",
            "at": "2022-03-01T10:15:00"
          },
          "carrierCode": "SQ",
          "number": "2050",
          "aircraft": {
            "code": "32N"
          },
          "operating": {
            "carrierCode": "LH"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "45",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "AMS",
            "at": "2022-03-01T13:05:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:40:00"
          },
          "carrierCode": "AY",
          "number": "4133",
          "aircraft": {
            "code": "789"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "G"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "28",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT11H20M",
      "segments": [
        {
          "id": "1",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T09:55:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T14:15:00"
          },
          "carrierCode": "UA",
          "number": "8864",
          "aircraft": {
            "code": "333"
          },
          "operating": {
            "carrierCode": "LH"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "T"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "29",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT11H20M",
      "segments": [
        {
          "id": "2",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T09:55:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T14:15:00"
          },
          "carrierCode": "LH",
          "number": "438",
          "aircraft": {
            "code": "333"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "30",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H",
      "segments": [
        {
          "id": "24",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T09:55:00"
          },
          "arrival": {
            "iataCode": "YUL",
            "at": "2022-03-01T11:35:00"
          },
          "carrierCode": "6X",
          "number": "9734",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            }
          ]
        },
        {
          "id": "25",
          "numberOfStops": 0,
          "blacklistedInEU": False,
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
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "31",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H",
      "segments": [
        {
          "id": "26",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "at": "2022-03-01T09:55:00"
          },
          "arrival": {
            "iataCode": "YUL",
            "at": "2022-03-01T11:35:00"
          },
          "carrierCode": "7X",
          "number": "234",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "X"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            }
          ]
        },
        {
          "id": "27",
          "numberOfStops": 0,
          "blacklistedInEU": False,
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
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "32",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H35M",
      "segments": [
        {
          "id": "8",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T10:00:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "terminal": "2",
            "at": "2022-03-01T10:45:00"
          },
          "carrierCode": "LH",
          "number": "904",
          "aircraft": {
            "code": "32N"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "9",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "5",
            "at": "2022-03-01T12:15:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T16:35:00"
          },
          "carrierCode": "IB",
          "number": "7388",
          "aircraft": {
            "code": "781"
          },
          "operating": {
            "carrierCode": "BA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "33",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H50M",
      "segments": [
        {
          "id": "20",
          "numberOfStops": 0,
          "blacklistedInEU": False,
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
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "21",
          "numberOfStops": 0,
          "blacklistedInEU": False,
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
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "34",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H40M",
      "segments": [
        {
          "id": "46",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T10:45:00"
          },
          "arrival": {
            "iataCode": "ORD",
            "terminal": "5",
            "at": "2022-03-01T13:05:00"
          },
          "carrierCode": "LH",
          "number": "430",
          "aircraft": {
            "code": "74H"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 2,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "W"
            }
          ]
        },
        {
          "id": "47",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "ORD",
            "terminal": "1",
            "at": "2022-03-01T15:50:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T18:25:00"
          },
          "carrierCode": "LH",
          "number": "7468",
          "aircraft": {
            "code": "319"
          },
          "operating": {
            "carrierCode": "UA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 2,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "W"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "35",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT11H10M",
      "segments": [
        {
          "id": "3",
          "numberOfStops": 0,
          "blacklistedInEU": False,
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
          "carrierCode": "IB",
          "number": "4203",
          "aircraft": {
            "code": "787"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "36",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H45M",
      "segments": [
        {
          "id": "68",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T11:00:00"
          },
          "arrival": {
            "iataCode": "JFK",
            "terminal": "1",
            "at": "2022-03-01T13:35:00"
          },
          "carrierCode": "LH",
          "number": "400",
          "aircraft": {
            "code": "388"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 8,
              "class": "F"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            }
          ]
        },
        {
          "id": "69",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LGA",
            "terminal": "B",
            "at": "2022-03-01T16:26:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "0",
            "at": "2022-03-01T19:45:00"
          },
          "carrierCode": "B6",
          "number": "4206",
          "aircraft": {
            "code": "321"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "P"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "37",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H25M",
      "segments": [
        {
          "id": "60",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T11:10:00"
          },
          "arrival": {
            "iataCode": "IAD",
            "at": "2022-03-01T14:15:00"
          },
          "carrierCode": "UA",
          "number": "988",
          "aircraft": {
            "code": "777"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        },
        {
          "id": "61",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "IAD",
            "at": "2022-03-01T17:16:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T19:35:00"
          },
          "carrierCode": "UA",
          "number": "212",
          "aircraft": {
            "code": "319"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "38",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H25M",
      "segments": [
        {
          "id": "62",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T11:10:00"
          },
          "arrival": {
            "iataCode": "IAD",
            "at": "2022-03-01T14:15:00"
          },
          "carrierCode": "LH",
          "number": "9290",
          "aircraft": {
            "code": "777"
          },
          "operating": {
            "carrierCode": "UA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "T"
            }
          ]
        },
        {
          "id": "63",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "IAD",
            "at": "2022-03-01T17:16:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T19:35:00"
          },
          "carrierCode": "UA",
          "number": "212",
          "aircraft": {
            "code": "319"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "39",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H10M",
      "segments": [
        {
          "id": "30",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T12:00:00"
          },
          "arrival": {
            "iataCode": "LHR",
            "terminal": "2",
            "at": "2022-03-01T12:45:00"
          },
          "carrierCode": "LH",
          "number": "906",
          "aircraft": {
            "code": "32N"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        },
        {
          "id": "31",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "LHR",
            "terminal": "3",
            "at": "2022-03-01T14:45:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "D",
            "at": "2022-03-01T19:10:00"
          },
          "carrierCode": "IB",
          "number": "4193",
          "aircraft": {
            "code": "77W"
          },
          "operating": {
            "carrierCode": "AA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 7,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "I"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 7,
              "class": "O"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "40",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H40M",
      "segments": [
        {
          "id": "16",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T12:55:00"
          },
          "arrival": {
            "iataCode": "IAD",
            "at": "2022-03-01T15:55:00"
          },
          "carrierCode": "UA",
          "number": "8827",
          "aircraft": {
            "code": "744"
          },
          "operating": {
            "carrierCode": "LH"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "T"
            }
          ]
        },
        {
          "id": "17",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "IAD",
            "at": "2022-03-01T17:16:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T19:35:00"
          },
          "carrierCode": "UA",
          "number": "212",
          "aircraft": {
            "code": "319"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "41",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT13H40M",
      "segments": [
        {
          "id": "18",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T12:55:00"
          },
          "arrival": {
            "iataCode": "IAD",
            "at": "2022-03-01T15:55:00"
          },
          "carrierCode": "LH",
          "number": "418",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            }
          ]
        },
        {
          "id": "19",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "IAD",
            "at": "2022-03-01T17:16:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T19:35:00"
          },
          "carrierCode": "UA",
          "number": "212",
          "aircraft": {
            "code": "319"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "42",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H8M",
      "segments": [
        {
          "id": "28",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T13:25:00"
          },
          "arrival": {
            "iataCode": "DEN",
            "at": "2022-03-01T15:45:00"
          },
          "carrierCode": "LH",
          "number": "446",
          "aircraft": {
            "code": "744"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            }
          ]
        },
        {
          "id": "29",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "DEN",
            "at": "2022-03-01T17:25:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T20:33:00"
          },
          "carrierCode": "UA",
          "number": "1235",
          "aircraft": {
            "code": "319"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 8,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "43",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT15H13M",
      "segments": [
        {
          "id": "56",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T13:25:00"
          },
          "arrival": {
            "iataCode": "YYZ",
            "terminal": "1",
            "at": "2022-03-01T16:05:00"
          },
          "carrierCode": "AC",
          "number": "9105",
          "aircraft": {
            "code": "744"
          },
          "operating": {
            "carrierCode": "LH"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "L"
            }
          ]
        },
        {
          "id": "57",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "YYZ",
            "terminal": "1",
            "at": "2022-03-01T19:05:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T21:38:00"
          },
          "carrierCode": "AC",
          "number": "7615",
          "aircraft": {
            "code": "E75"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "44",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H20M",
      "segments": [
        {
          "id": "34",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T13:50:00"
          },
          "arrival": {
            "iataCode": "IAH",
            "terminal": "E",
            "at": "2022-03-01T18:10:00"
          },
          "carrierCode": "LH",
          "number": "7601",
          "aircraft": {
            "code": "777"
          },
          "operating": {
            "carrierCode": "UA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "G"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "N"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "T"
            }
          ]
        },
        {
          "id": "35",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "IAH",
            "terminal": "C",
            "at": "2022-03-01T19:55:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T21:10:00"
          },
          "carrierCode": "LH",
          "number": "8661",
          "aircraft": {
            "code": "319"
          },
          "operating": {
            "carrierCode": "UA"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 4,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 4,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 3,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 6,
              "class": "T"
            }
          ]
        }
      ]
    },
    {
      "type": "flight-availability",
      "id": "45",
      "originDestinationId": "1",
      "source": "GDS",
      "instantTicketingRequired": False,
      "paymentCardRequired": False,
      "duration": "PT14H20M",
      "segments": [
        {
          "id": "36",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "FRA",
            "terminal": "1",
            "at": "2022-03-01T13:50:00"
          },
          "arrival": {
            "iataCode": "IAH",
            "terminal": "E",
            "at": "2022-03-01T18:10:00"
          },
          "carrierCode": "UA",
          "number": "47",
          "aircraft": {
            "code": "777"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "O"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "A"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "R"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        },
        {
          "id": "37",
          "numberOfStops": 0,
          "blacklistedInEU": False,
          "departure": {
            "iataCode": "IAH",
            "terminal": "C",
            "at": "2022-03-01T19:55:00"
          },
          "arrival": {
            "iataCode": "DFW",
            "terminal": "E",
            "at": "2022-03-01T21:10:00"
          },
          "carrierCode": "UA",
          "number": "1176",
          "aircraft": {
            "code": "319"
          },
          "availabilityClasses": [
            {
              "numberOfBookableSeats": 9,
              "class": "J"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "C"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "D"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Z"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "P"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Y"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "B"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "M"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "E"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "U"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "H"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "Q"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "V"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "W"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "S"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "T"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "L"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "K"
            },
            {
              "numberOfBookableSeats": 9,
              "class": "N"
            }
          ]
        }
      ]
    }
  ],
  "dictionaries": {
    "locations": {
      "ORD": {
        "cityCode": "CHI",
        "countryCode": "US"
      },
      "LAX": {
        "cityCode": "LAX",
        "countryCode": "US"
      },
      "LGA": {
        "cityCode": "NYC",
        "countryCode": "US"
      },
      "CDG": {
        "cityCode": "PAR",
        "countryCode": "FR"
      },
      "AMS": {
        "cityCode": "AMS",
        "countryCode": "NL"
      },
      "DEN": {
        "cityCode": "DEN",
        "countryCode": "US"
      },
      "IAD": {
        "cityCode": "WAS",
        "countryCode": "US"
      },
      "JFK": {
        "cityCode": "NYC",
        "countryCode": "US"
      },
      "DAL": {
        "cityCode": "DFW",
        "countryCode": "US"
      },
      "YUL": {
        "cityCode": "YMQ",
        "countryCode": "CA"
      },
      "IAH": {
        "cityCode": "HOU",
        "countryCode": "US"
      },
      "FRA": {
        "cityCode": "FRA",
        "countryCode": "DE"
      },
      "DFW": {
        "cityCode": "DFW",
        "countryCode": "US"
      },
      "LHR": {
        "cityCode": "LON",
        "countryCode": "GB"
      },
      "YYZ": {
        "cityCode": "YTO",
        "countryCode": "CA"
      },
      "LGW": {
        "cityCode": "LON",
        "countryCode": "GB"
      }
    }
  }
}