#!/usr/bin/python3
"""
state class model
"""
from models.base_model import BaseModel

class   State(BaseModel):
    """Represent a state
    Attributes:
        name (str): The name of the state
    """
    
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)