from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """Base class for all models."""
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)  # Call FileStorage's new() to register instance

    def save(self):
        """Updates `updated_at` and calls storage.save()."""
        self.updated_at = datetime.now()
        storage.save()  # Call FileStorage's save() to write to JSON

    def to_dict(self):
        """Converts instance to dictionary for JSON serialization."""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
