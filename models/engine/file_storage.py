import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the storage dictionary
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)  # Fixed typo (replaced . with ,)
        FileStorage.__objects[key] = obj
    
    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        all_objs = FileStorage.__objects
        obj_dict = {}
        
        for obj in all_objs.keys():  # Fixed typo (all_obj to all_objs)
            obj_dict[obj] = all_objs[obj].to_dict()
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:  # Fixed typos (replaced . with ,)
            json.dump(obj_dict, file)
        
    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:  # Fixed typos (replaced . with ,)
                try:
                    obj_dict = json.load(file)
                    
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        
                        cls = eval(class_name)  # Fixed typo (eva to eval)
                        
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass  # Fixed typo (expect expection to except Exception)
