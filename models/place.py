#!/usr/bin/python3
# Importing the BaseModel class from the base_model module
from models.base_model import BaseModel

# Defining the Place class, which inherits from BaseModel
class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    Represents a place with various attributes including city_id, user_id, and more.
    """
    
    # Public class attribute 'city_id', initialized to an empty string
    # Will store the ID of the City the place is located in
    city_id = ""
    
    # Public class attribute 'user_id', initialized to an empty string
    # Will store the ID of the User who owns the place
    user_id = ""
    
    # Public class attribute 'name', initialized to an empty string
    # Represents the name of the place
    name = ""
    
    # Public class attribute 'description', initialized to an empty string
    # Represents the description of the place
    description = ""
    
    # Public class attribute 'number_rooms', initialized to 0
    # Represents the number of rooms in the place
    number_rooms = 0
    
    # Public class attribute 'number_bathrooms', initialized to 0
    # Represents the number of bathrooms in the place
    number_bathrooms = 0
    
    # Public class attribute 'max_guest', initialized to 0
    # Represents the maximum number of guests the place can accommodate
    max_guest = 0
    
    # Public class attribute 'price_by_night', initialized to 0
    # Represents the price per night for staying at the place
    price_by_night = 0
    
    # Public class attribute 'latitude', initialized to 0.0
    # Represents the latitude of the place's location
    latitude = 0.0
    
    # Public class attribute 'longitude', initialized to 0.0
    # Represents the longitude of the place's location
    longitude = 0.0
    
    # Public class attribute 'amenity_ids', initialized to an empty list
    # Will store a list of Amenity IDs that belong to the place
    amenity_ids = []
