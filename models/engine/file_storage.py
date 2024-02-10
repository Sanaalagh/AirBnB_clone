#!/usr/bin/python3
"""File Storage Module"""
"""This module defines a class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances"""


import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

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
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    cls_name = val['__class__']
                    del val['__class__']
                    cls = eval(cls_name)
                    self.new(cls(**val))
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of supported classes for serialization"""
        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

