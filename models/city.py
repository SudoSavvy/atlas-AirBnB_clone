# Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel

# Define the City class that inherits from BaseModel
class City(BaseModel):
    """Represents a city for Airbnb."""
    
    # Public class attribute 'state_id', initialized as an empty string
    state_id = ""
    
    # Public class attribute 'name', initialized as an empty string
    name = ""

    # Constructor method for initializing a City instance
    def __init__(self, *args, **kwargs):
        """
        Initializes a City instance.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically containing instance data.
        """
        # Call the __init__ method of the superclass (BaseModel)
        super().__init__(*args, **kwargs)
