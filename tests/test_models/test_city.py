#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance_creation(self):
        """Test creation of City instance."""
        city = City()
        self.assertIsInstance(city, City)

    def test_attribute_setting(self):
        """Test setting attributes of City instance."""
        city = City(name="San Francisco", state_id="CA")
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, "CA")


if __name__ == '__main__':
    unittest.main()
