import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Class that serializes and deserializes instances to and from a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Loads the objects from a JSON file."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objs = json.load(file)
                for key, value in objs.items():
                    cls_name = value.pop('__class__')
                    self.new(eval(cls_name)(**value))
        # Optionally, you can handle the case where the file does not exist silently
