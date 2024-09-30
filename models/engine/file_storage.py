import json
import os

class FileStorage:
    """Class to manage file storage for AirBnB clone."""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or all objects of a specific class."""
        if cls is None:
            return self.__objects
        else:
            return {key: value for key, value in self.__objects.items() if isinstance(value, cls)}

    def get(self, cls_name, obj_id):
        """Retrieves an object based on its class name and id."""
        key = f"{cls_name}.{obj_id}"
        return self.__objects.get(key)

    def new(self, obj):
        """Adds a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves all objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Loads objects from the JSON file."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value['__class__']
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)

    def destroy(self, cls_name, obj_id):
        """Deletes an instance based on the class name and id."""
        key = f"{cls_name}.{obj_id}"
        if key in self.__objects:
            del self.__objects[key]
            self.save()
            return True
        return False
