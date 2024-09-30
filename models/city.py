#!/usr/bin/python3
"""Module that defines the City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel."""

    state_id = ""  # Public class attribute representing the state ID, initialized as an empty string.
    name = ""      # Public class attribute representing the city name, initialized as an empty string.

    def __init__(self, *args, **kwargs):
        """Initialize the City instance, calling the parent constructor."""
        super().__init__(*args, **kwargs)  # Call the super class (BaseModel) constructor.
