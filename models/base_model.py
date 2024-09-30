from datetime import datetime
import uuid

class BaseModel:
    """Base model class for all objects."""
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the instance into a dictionary."""
        return {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    def save(self):
        """Updates the updated_at attribute and saves the instance."""
        self.updated_at = datetime.now()
        global storage  # Make sure to declare storage as global
        storage.new(self)
        storage.save()
        