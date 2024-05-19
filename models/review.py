#!/usr/bin/python3
"""
review class model
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review
    Attributes:
        place_id (str): The Place id
        user_id (str): The User id
        text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)