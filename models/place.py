# Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel

# Define the Place class that inherits from BaseModel
class Place(BaseModel):
    """Represents a place for Airbnb."""
    
    # Public class attribute 'city_id', stores the id of the city (empty string by default)
    city_id = ""
    
    # Public class attribute 'user_id', stores the id of the user (empty string by default)
    user_id = ""
    
    # Public class attribute 'name', stores the name of the place (empty string by default)
    name = ""
    
    # Public class attribute 'description', stores the description of the place (empty string by default)
    description = ""
    
    # Public class attribute 'number_rooms', stores the number of rooms (initialized to 0)
    number_rooms = 0
    
    # Public class attribute 'number_bathrooms', stores the number of bathrooms (initialized to 0)
    number_bathrooms = 0
    
    # Public class attribute 'max_guest', stores the maximum number of guests (initialized to 0)
    max_guest = 0
    
    # Public class attribute 'price_by_night', stores the price per night (initialized to 0)
    price_by_night = 0
    
    # Public class attribute 'latitude', stores the latitude as a floating point number (initialized to 0.0)
    latitude = 0.0
    
    # Public class attribute 'longitude', stores the longitude as a floating point number (initialized to 0.0)
    longitude = 0.0
    
    # Public class attribute 'amenity_ids', stores a list of amenity ids (empty list by default)
    amenity_ids = []

    # Constructor method for initializing a Place instance
    def __init__(self, *args, **kwargs):
        """
        Initializes a Place instance.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, typically containing instance data.
        """
        # Call the __init__ method of the superclass (BaseModel)
        super().__init__(*args, **kwargs)
