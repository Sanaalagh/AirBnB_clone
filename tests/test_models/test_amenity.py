#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance_creation(self):
        """Test creation of Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attribute_setting(self):
        """Test setting attributes of Amenity instance."""
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

if __name__ == '__main__':
    unittest.main()
