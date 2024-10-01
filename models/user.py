# Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel

# Define the User class that inherits from BaseModel
class User(BaseModel):
    """Represents a user for Airbnb."""
    
    # Public class attribute 'email', stores the email of the user (empty string by default)
    email = ""
    
    # Public class attribute 'password', stores the password of the user (empty string by default)
    password = ""
    
    # Public class attribute 'first_name', stores the first name of the user (empty string by default)
    first_name = ""
    
    # Public class attribute 'last_name', stores the last name of the user (empty string by default)
    last_name = ""

    # Constructor method for initializing a User instance
    def __init__(self, *args, **kwargs):
        """
        Initializes a User instance.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically containing instance data.
        """
        # Call the __init__ method of the superclass (BaseModel)
        super().__init__(*args, **kwargs)
