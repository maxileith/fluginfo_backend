import unittest
from amadeus_connector.utils import duration_to_minutes, inches_to_cm, split_flight_number
from amadeus_connector.errors import AmadeusBadRequest


class TestUtils(unittest.TestCase):

    def test_duration_to_minutes(self):
        self.assertEqual(duration_to_minutes('PT1H1M'), 61)
        self.assertEqual(duration_to_minutes('PT3H22M'), 202)
        self.assertEqual(duration_to_minutes('PT0H25M'), 25)
        self.assertEqual(duration_to_minutes('PT42M'), 42)
        self.assertEqual(duration_to_minutes('PT2H'), 120)
        with self.assertRaises(AmadeusBadRequest):
            duration_to_minutes('abc')

    def test_inches_to_cm(self):
        self.assertEqual(inches_to_cm(1.1), round(2.54))

    def test_split_flight_number(self):
        self.assertEqual(split_flight_number('LH438'), ('LH', 438))
        self.assertEqual(split_flight_number('EK48'), ('EK', 48))
        self.assertEqual(split_flight_number('X31234'), ('X3', 1234))
        with self.assertRaises(AmadeusBadRequest):
            split_flight_number('ABC12')


if __name__ == '__main__':
    unittest.main()
