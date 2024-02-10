#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class
    Public class attributes:
    name: string - empty string
    """
    name = ""


def __init__(self, *args, **kwargs):
    """Initialization method for Amenity"""
    super().__init__(*args, **kwargs)
