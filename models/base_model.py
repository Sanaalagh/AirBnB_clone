#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class for other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """
        initalisation of an object with it's
        attributes
        Args :
                Args(won't be used ): list of arguments
                Kwargs: pass in dictionary as arguments
        """
        if kwargs:
            for key, v in kwargs.items():
                if key != '__class__':
                    setattr(self, key, v)
                elif key in ('created_at', 'updated_at'):
                    Nv = datetime.fromisoformat(v)
                    setattr(self, key, Nv)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation
        of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

    def __str__(self):
        """Returns a string representation
        of the BaseModel instance"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
