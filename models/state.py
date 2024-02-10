#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """
    State class
    Public class attributes:
    name: string - empty string
    """
    name = ""

def __init__(self, *args, **kwargs):
        """Initialization method for State"""
        super().__init__(*args, **kwargs)
