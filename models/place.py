#!/usr/bin/python3
"""Module that defines the Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class that inherits from BaseModel."""

    city_id = ""         # Public class attribute representing the city ID, initialized as an empty string.
    user_id = ""         # Public class attribute representing the user ID, initialized as an empty string.
    name = ""            # Public class attribute representing the name of the place, initialized as an empty string.
    description = ""     # Public class attribute representing the description of the place, initialized as an empty string.
    number_rooms = 0     # Public class attribute representing the number of rooms, initialized as 0.
    number_bathrooms = 0 # Public class attribute representing the number of bathrooms, initialized as 0.
    max_guest = 0        # Public class attribute representing the maximum number of guests, initialized as 0.
    price_by_night = 0   # Public class attribute representing the price per night, initialized as 0.
    latitude = 0.0       # Public class attribute representing the latitude of the place, initialized as 0.0.
    longitude = 0.0      # Public class attribute representing the longitude of the place, initialized as 0.0.
    amenity_ids = []     # Public class attribute representing a list of amenity IDs, initialized as an empty list.

    def __init__(self, *args, **kwargs):
        """Initialize the Place instance, calling the parent constructor."""
        super().__init__(*args, **kwargs)  # Call the super class (BaseModel) constructor.
