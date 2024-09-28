import json
from models.base_model import BaseModel

class Filestorage:
    """Serialises instances to a JSON file and deserialises back to instances."""

    __file_path = "file.json" # Path to the JSON file
    __objects = {} # Will store all objects in <class name>.id format

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Seriaalizes __objects to the JSON file."""
        obj_dict = {key : obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialises the JSON file to __objects if the file exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj['__class__']
                    if cls_name == 'BaseModel':
                        FileStorage.__objects[obj['__class__'] + "." + obj['id']] = BaseModel (**obj)
        except FileNotFoundError:
            pass # If the file doesn't exist, do nothing