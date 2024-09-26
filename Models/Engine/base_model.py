import uuid  # Import the uuid module to generate unique identifiers
from datetime import datetime  # Import datetime for handling date and time

class BaseModel:
    """BaseModel defines all common attributes and methods for other classes."""

    def __init__(self):
        """Initialize a new BaseModel instance with unique ID and timestamps."""
        self.id = str(uuid.uuid4())  # Generate a unique ID and convert it to a string
        self.created_at = datetime.now()  # Set the creation time to the current datetime
        self.updated_at = datetime.now()  # Set the updated time to the current datetime

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
