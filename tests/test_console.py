#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage

class TestConsole(unittest.TestCase):
    """Test cases for console.py"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up test environment"""
        del self.console

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue(), "\n")

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("count"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_invalid_command(self):
        """Test invalid command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid")
            self.assertEqual(f.getvalue(), "*** Unknown syntax: invalid\n")

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help"))
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    # Add more test cases for other commands...

if __name__ == '__main__':
    unittest.main()
