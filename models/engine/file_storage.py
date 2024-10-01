# Import the json module for handling JSON data
import json

# Import necessary classes from the models module
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Define the FileStorage class to manage the storage of model instances in JSON format
class FileStorage:
    """FileStorage class to manage
    storage of model instances in JSON format."""
    
    # Private class attribute to store the file path for the JSON file
    __file_path = "file.json"
    
    # Private class attribute to hold the dictionary of stored objects
    __objects = {}

    # Method to return the dictionary of stored objects
    def all(self):
        """Returns the dictionary of stored objects."""
        return FileStorage.__objects

    # Method to add a new object to the storage
    def new(self, obj):
        """Adds a new object to the storage."""
        if obj:  # Check if the object is not None
            # Create a key using the object's class name and id
            key = f"{type(obj).__name__}.{obj.id}"
            # Store the object in the __objects dictionary with the generated key
            FileStorage.__objects[key] = obj

    # Method to save the stored objects to a JSON file
    def save(self):
        """Saves the stored objects to a JSON file."""
        # Open the JSON file in write mode
        with open(FileStorage.__file_path, 'w') as f:
            # Dump the dictionary of objects into the JSON file
            json.dump(self.to_dict(), f)

    # Method to convert all stored objects to a dictionary format
    def to_dict(self):
        """Converts all stored objects to a dictionary format."""
        return {
            # Use dictionary comprehension to create a new dictionary
            key: obj.to_dict()  # Convert each object to dictionary format
            for key, obj in FileStorage.__objects.items()
        }

    # Method to load the stored objects from a JSON file
    def reload(self):
        """Loads the stored objects from a JSON file."""
        try:
            # Open the JSON file in read mode
            with open(FileStorage.__file_path, 'r') as f:
                # Load the JSON data from the file
                objects = json.load(f)
                # Iterate over the loaded objects
                for key, value in objects.items():
                    # Get the class name of the object
                    class_name = value["__class__"]
                    # Create an object based on its class name
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
                        continue  # Skip unknown class names
                    # Add the new object to storage
                    self.new(obj)
        except FileNotFoundError:
            pass  # Handle case when the file does not exist
