import uuid  # Import the uuid module to generate unique identifiers
from datetime import datetime  # Import datetime for handling date and time

class BaseModel:
    """BaseModel defines all common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.
        If kwargs is provided, use it to recreate the instance from a dictionary.
        Otherwise, create a new instance with unique ID and timestamps.
        """
        if kwargs:
            # Iterate over kwargs to set each attribute
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert string to datetime for these attributes
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    # Set the attribute on the instance, but ignore __class__
                    setattr(self, key, value)
        else:
            # Create a new instance with unique ID and current timestamps
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()  # Set the creation time
            self.updated_at = datetime.now()  # Set the update time

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        # Format the string to include the class name, ID, and instance attributes
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()  # Update the updated_at to the current datetime

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        # Create a dictionary from the instance's __dict__ (attributes)
        dict_representation = self.__dict__.copy()  # Copy the instance's attributes
        dict_representation['__class__'] = self.__class__.__name__  # Add class name to the dictionary
        # Convert datetime attributes to ISO format for serialization
        dict_representation['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO format
        dict_representation['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO format
        return dict_representation  # Return the dictionary representation
