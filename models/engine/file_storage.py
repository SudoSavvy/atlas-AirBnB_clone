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
        try:
            with open(self.__file_path, 'w') as f:
                json.dump(obj_dict, f)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value.get("__class__")
                    if class_name and class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            print("File not found, nothing to reload.")
        except json.JSONDecodeError:
            print("Error decoding JSON file.")
        except Exception as e:
            print(f"Unexpected error during reload: {e}")
