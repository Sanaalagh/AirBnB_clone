#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance_creation(self):
        """Test creation of Place instance."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attribute_setting(self):
        """Test setting attributes of Place instance."""
        place = Place(name="Cozy Cabin", city_id="123", user_id="456")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")

if __name__ == '__main__':
    unittest.main()
