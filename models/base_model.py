import uuid
from datetime import datetime
import models.storage

class BaseModel:
    """BaseModel class that defines common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute and saves the instance."""
        self.updated_at = datetime.now()
        models.storage.storage.new(self)  # Use the global storage instance
        models.storage.storage.save()

    def __str__(self):
        """Returns the string representation of the BaseModel."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
