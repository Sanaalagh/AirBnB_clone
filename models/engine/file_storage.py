#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""File Storage Module"""
"""This module defines a class FileStorage
that serializes instances to a JSON
file and deserializes JSON file to instances"""


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as file:
            serialized_objects = {}
            for k, v in self.__objects.items():
                if hasattr(v, 'to_dict') and callable(getattr(v, 'to_dict')):
                    serialized_objects[k] = v.to_dict()
                else:
                    serialized_objects[k] = v
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        current_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'State': State,
            'Place': Place,
            'Review': Review
            }

        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as file:
            deserialized = None

            try:
                deserialized = json.load(file)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            self.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
