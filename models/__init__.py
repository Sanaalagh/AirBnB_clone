#!/usr/bin/python3
"""
Initialization module for the engine package.

This module imports the `FileStorage` class from the `file_storage` module
and creates a global instance of `FileStorage` named `storage`. It also
calls the `reload()` method of the `storage` instance to load any previously
stored data from the JSON file into memory.
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Create a global instance of FileStorage
storage = FileStorage()

# Load any previously stored data from the JSON file into memory
storage.reload()
# Add User class to the classes dictionary
classes = {
    'BaseModel': BaseModel,
    'User': User,  # Add the User class here
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}
