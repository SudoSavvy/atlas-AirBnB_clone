#!/usr/bin/python3
"""Module that defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel."""

    place_id = ""  # Public class attribute representing the place ID, initialized as an empty string.
    user_id = ""   # Public class attribute representing the user ID, initialized as an empty string.
    text = ""      # Public class attribute representing the review text, initialized as an empty string.

    def __init__(self, *args, **kwargs):
        """Initialize the Review instance, calling the parent constructor."""
        super().__init__(*args, **kwargs)  # Call the super class (BaseModel) constructor.
