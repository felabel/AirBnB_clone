#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file _file_path to _objects, if it exists."""
        try:
            with open(self._file_path) as f:
                obj_dict = json.load(f)
                for obj_key, obj_data in obj_dict.items():
                    cls_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    obj_instance = globals()[cls_name](**obj_data)
                    self._objects[obj_key] = obj_instance
        except (json.JSONDecodeError, FileNotFoundError):
            pass