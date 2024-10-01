from datetime import datetime  # Importing datetime to handle date and time.
import uuid  # Importing uuid to generate unique identifiers for each instance.

class BaseModel:
    """Base class for all models in the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs are provided, sets instance attributes based on them.
        If no kwargs are provided, generates a new id, created_at, and updated_at attributes.
        """
        if kwargs:
            # If kwargs is passed, iterate through its key-value pairs.
            for key, value in kwargs.items():
                # Exclude the '__class__' attribute from being set.
                if key != '__class__':
                    setattr(self, key, value)  # Set the attribute on the instance.

            # If 'created_at' is in kwargs, convert its string format to a datetime object.
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            # If 'updated_at' is in kwargs, convert its string format to a datetime object.
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            # If no kwargs, create a new id for the instance using uuid4.
            self.id = str(uuid.uuid4())

            # Assign the current datetime to the created_at attribute.
            self.created_at = datetime.now()

            # Assign the current datetime to the updated_at attribute.
            self.updated_at = datetime.now()

            # Import storage inside the method to avoid circular imports with the models module.
            from models import storage

            # Register the newly created instance with the storage engine.
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute to the current time and saves the object to storage.
        """
        # Set updated_at to the current time to reflect the latest save.
        self.updated_at = datetime.now()

        # Import storage inside the method to avoid circular imports with the models module.
        from models import storage

        # Save all objects to storage (which could be to a file or database).
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance, including class name and ISO format of datetime attributes.
        """
        # Copy the instance's __dict__ (attributes) to a new dictionary.
        new_dict = self.__dict__.copy()

        # Add the class name of the instance to the dictionary.
        new_dict['__class__'] = self.__class__.__name__

        # Convert created_at to ISO format for easier serialization.
        new_dict['created_at'] = self.created_at.isoformat()

        # Convert updated_at to ISO format for easier serialization.
        new_dict['updated_at'] = self.updated_at.isoformat()

        # Return the dictionary containing all instance attributes.
        return new_dict
