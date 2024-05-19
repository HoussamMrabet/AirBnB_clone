#!/usr/bin/python3
"""
Defines the User class.
"""
from models.base_model import BaseModel
class user(BaseModel):
    """Represent a User
    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name =   ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)