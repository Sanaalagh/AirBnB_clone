#!/usr/bin/python3
"""
Initialization module for the engine package.

This module imports the `FileStorage` class from the `file_storage` module
and creates a global instance of `FileStorage` named `storage`. It also
calls the `reload()` method of the `storage` instance to load any previously
stored data from the JSON file into memory.
"""

from models.engine.file_storage import FileStorage

# Create a global instance of FileStorage
storage = FileStorage()

# Load any previously stored data from the JSON file into memory
storage.reload()
