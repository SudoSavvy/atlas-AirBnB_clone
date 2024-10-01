# Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel

# Define the Amenity class that inherits from BaseModel
class Amenity(BaseModel):
    """Represents an amenity for Airbnb."""
    
    # Public class attribute 'name', initialized as an empty string
    name = ""

    # Constructor method for initializing an Amenity instance
    def __init__(self, *args, **kwargs):
        """
        Initializes an Amenity instance.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically containing instance data.
        """
        # Call the __init__ method of the superclass (BaseModel)
        super().__init__(*args, **kwargs)
