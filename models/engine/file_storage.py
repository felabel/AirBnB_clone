import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine."""

    def __init__(self):
        """Initialize FileStorage with instance attributes."""
        self._file_path = "file.json"
        self._objects = {}

    def all(self):
        """Return the dictionary _objects."""
        return self._objects

    def new(self, obj):
        """Set in _objects obj with key <obj_class_name>.id"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self._objects[obj_key] = obj

    def save(self):
        """Serialize _objects to the JSON file _file_path."""
        obj_dict = {key: obj.to_dict() for key, obj in self._objects.items()}
        with open(self._file_path, "w") as f:
            json.dump(obj_dict, f)

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
