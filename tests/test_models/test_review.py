#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance_creation(self):
        """Test creation of Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attribute_setting(self):
        """Test setting attributes of Review instance."""
        review = Review(text="Great experience", user_id="789", place_id="012")
        self.assertEqual(review.text, "Great experience")
        self.assertEqual(review.user_id, "789")
        self.assertEqual(review.place_id, "012")

if __name__ == '__main__':
    unittest.main()
