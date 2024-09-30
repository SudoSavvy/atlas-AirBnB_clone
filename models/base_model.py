#!/usr/bin/python3
"""Module that defines the BaseModel class."""
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class that defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()  # Set the creation time to now
            self.updated_at = self.created_at  # Set the updated time to the same as creation
            from models import storage  # Delayed import to avoid circular import
            storage.new(self)  # Add the new instance to storage

    def save(self):
        """Update the updated_at attribute and save the object to file storage."""
        self.updated_at = datetime.now()  # Update the time of last modification
        from models import storage  # Delayed import to avoid circular import
        storage.save()  # Save the instance to file storage

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        my_dict = self.__dict__.copy()  # Copy the instance attributes to a new dictionary
        my_dict["__class__"] = self.__class__.__name__  # Add the class name to the dictionary
        my_dict["created_at"] = self.created_at.isoformat()  # Convert created_at to string format
        my_dict["updated_at"] = self.updated_at.isoformat()  # Convert updated_at to string format
        return my_dict
