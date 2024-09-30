#!/usr/bin/python3
"""Module that defines the Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""

    name = ""  # Public class attribute representing the name of the amenity, initialized as an empty string.

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity instance, calling the parent constructor."""
        super().__init__(*args, **kwargs)  # Call the super class (BaseModel) constructor.
