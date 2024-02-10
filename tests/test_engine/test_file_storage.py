#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_instance_creation(self):
        """Test creation of FileStorage instance."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

if __name__ == '__main__':
    unittest.main()
