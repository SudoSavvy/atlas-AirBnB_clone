import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_initialization(self):
        """Test that a Place instance is created correctly."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test default attributes of Place."""
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)


if __name__ == '__main__':
    unittest.main()
