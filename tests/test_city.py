import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_initialization(self):
        """Test that a City instance is created correctly."""
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """Test default attributes of City."""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == '__main__':
    unittest.main()
