import unittest
from unittest.mock import Mock, MagicMock
from amadeus.client.errors import ServerError, ClientError, NotFoundError
from tests.amadeus_client_mock import AmadeusMockClient, AmadeusResponse
from amadeus_connector.flightroute import FlightRoute
from amadeus_connector.errors import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError


class TestFlightRoute(unittest.TestCase):

    def setUp(self):
        self.amadeus_client = AmadeusMockClient()
        self.flight_route = FlightRoute(self.amadeus_client)

    def test_flight_route_success(self):
        self.assertDictEqual(self.flight_route.get('LH438', '2022-03-01'), {
            "departureIata": "FRA",
            "arrivalIata": "DFW"
        })
        self.assertDictEqual(self.flight_route.get_advanced('LH', 438, '2022-03-01'), {
            "departureIata": "FRA",
            "arrivalIata": "DFW"
        })

    def test_flight_route_error(self):
        # server error
        self.amadeus_client.schedule.flights.get = Mock(
            side_effect=ServerError(None))
        with self.assertRaises(AmadeusServerError):
            self.flight_route.get('LH438', '2022-03-01')
        with self.assertRaises(AmadeusServerError):
            self.flight_route.get_advanced('LH', 438, '2022-03-01')
        # client error
        self.amadeus_client.schedule.flights.get = Mock(
            side_effect=ClientError(None))
        with self.assertRaises(AmadeusBadRequest):
            self.flight_route.get('LH438', '2022-03-01')
        with self.assertRaises(AmadeusBadRequest):
            self.flight_route.get_advanced('LH', 438, '2022-03-01')
        # nothing found 1
        self.amadeus_client.schedule.flights.get = Mock(
            side_effect=NotFoundError(None))
        with self.assertRaises(AmadeusNothingFound):
            self.flight_route.get('LH438', '2022-03-01')
        with self.assertRaises(AmadeusNothingFound):
            self.flight_route.get_advanced('LH', 438, '2022-03-01')
        # nothing found 2
        self.amadeus_client.schedule.flights.get = MagicMock(
            return_value=AmadeusResponse({'data': []})
        )
        with self.assertRaises(AmadeusNothingFound):
            self.flight_route.get('LH438', '2022-03-01')
        with self.assertRaises(AmadeusNothingFound):
            self.flight_route.get_advanced('LH', 438, '2022-03-01')


if __name__ == '__main__':
    unittest.main()
