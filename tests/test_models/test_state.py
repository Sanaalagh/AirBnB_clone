#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class."""
    
    def test_instance_creation(self):
        """Test creation of State instance."""
        state = State()
        self.assertIsInstance(state, State)

    def test_attribute_setting(self):
        """Test setting attributes of State instance."""
        state = State(name="California")
        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()
