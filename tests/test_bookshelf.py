import unittest
from amadeus_connector.bookshelf import Bookshelf
from amadeus_connector.errors import AmadeusNothingFound


class TestBookshelf(unittest.TestCase):

    def setUp(self):
        self.bookshelf = Bookshelf(
            {
                'type1': {
                    'item1': 1,
                    'item2': 2,
                    'item3': 3,
                },
                'type2': {},
            }
        )

    def test_get_success(self):
        self.assertEqual(self.bookshelf.get('type1', 'item1'), 1)
        self.assertEqual(self.bookshelf.get('type1', 'item2'), 2)
        self.assertEqual(self.bookshelf.get('type1', 'item3'), 3)

    def test_get_nothing_found(self):
        with self.assertRaises(AmadeusNothingFound):
            self.bookshelf.get('type1', 'item42')
        with self.assertRaises(AmadeusNothingFound):
            self.bookshelf.get('type2', 'item1')
        with self.assertRaises(AmadeusNothingFound):
            self.bookshelf.get('type3', 'item1')

    def test_add_new(self):
        self.bookshelf.add(
            type3={
                'item1': 10,
                'item2': 11,
                'item3': 12,
            },
        )
        self.assertEqual(self.bookshelf.get('type3', 'item1'), 10)
        self.assertEqual(self.bookshelf.get('type3', 'item2'), 11)
        self.assertEqual(self.bookshelf.get('type3', 'item3'), 12)

    def test_add_overwrite(self):
        self.bookshelf.add(
            type1={
                'item1': 42,
                'item2': 43,
                'item3': 44,
            },
        )
        self.assertEqual(self.bookshelf.get('type1', 'item1'), 42)
        self.assertEqual(self.bookshelf.get('type1', 'item2'), 43)
        self.assertEqual(self.bookshelf.get('type1', 'item3'), 44)

    def test_add_multiple(self):
        self.bookshelf.add(
            type3={
                'item1': 42,
            },
            type4={
                'item1': 43,
            },
        )
        self.assertEqual(self.bookshelf.get('type3', 'item1'), 42)
        self.assertEqual(self.bookshelf.get('type4', 'item1'), 43)


if __name__ == '__main__':
    unittest.main()
