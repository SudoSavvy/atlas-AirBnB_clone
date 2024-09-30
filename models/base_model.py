import uuid
from datetime import datetime


class BaseModel:
    """Base model for all classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute."""
        self.updated_at = datetime.now()
        storage.new(self)

    def to_dict(self):
        """Converts the instance to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
        }
