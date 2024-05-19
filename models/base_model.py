#!/usr/bin/python3
import uuid
from datetime import datetime
import models.engine

class BaseModel:
    #instance attribut
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        models.engine.storage.new(self)

    #instance method
    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        
        return instance_dict
    
    def save(self):
        self.updated_at = datetime.now()
        models.engine.storage.save()
    
    def __str__(self):
        instance_dict = self.to_dict()
        return f"[{self.__class__.__name__}] ({instance_dict['id']}) {instance_dict}"

