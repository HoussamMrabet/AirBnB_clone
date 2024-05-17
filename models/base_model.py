#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    #instance attribute
    def __init__(self, my_number=None, name=None):
        self.my_number = my_number
        self.name = name
        self.updated_at = datetime.now()
        self.id = uuid.uuid4()
        self.created_at = datetime.now()

    #instance method
    
    def to_dict(self):
        instance_dict = self.__dict__.copy()
        
        if self.created_at:
            instance_dict['created_at'] = self.created_at.isoformat()
        if self.updated_at:
            instance_dict['updated_at'] = self.updated_at.isoformat()
        
        return instance_dict
    
    def save(self):
        self.updated_at = datetime.now()
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

