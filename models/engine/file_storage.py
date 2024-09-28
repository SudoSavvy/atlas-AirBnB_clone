import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file & deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                print("Object data loaded from JSON:", obj_dict)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    print(f"Reloading object: {key} (class: {class_name})")
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
