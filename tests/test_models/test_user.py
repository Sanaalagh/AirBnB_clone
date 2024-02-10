#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_instance_creation(self):
        """Test creation of User instance."""
        user = User()
        self.assertIsInstance(user, User)

    def test_attribute_setting(self):
        """Test setting attributes of User instance."""
        user = User(email="test@example.com", password="password")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")

if __name__ == '__main__':
    unittest.main()
