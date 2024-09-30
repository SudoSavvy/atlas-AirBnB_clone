import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage class to manage storage of model instances in JSON format."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves the stored objects to a JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(self.to_dict(), f)

    def to_dict(self):
        """Converts all stored objects to a dictionary format."""
        return {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}

    def reload(self):
        """Loads the stored objects from a JSON file."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    elif class_name == "Place":
                        obj = Place(**value)
                    elif class_name == "State":
                        obj = State(**value)
                    elif class_name == "City":
                        obj = City(**value)
                    elif class_name == "Amenity":
                        obj = Amenity(**value)
                    elif class_name == "Review":
                        obj = Review(**value)
                    else:
                        continue
                    self.new(obj)
        except FileNotFoundError:
            pass  # Handle case when file does not exist
