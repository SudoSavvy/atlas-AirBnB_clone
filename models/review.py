#!/usr/bin/python3
# Importing the BaseModel class from the base_model module
from models.base_model import BaseModel

# Defining the Review class, which inherits from BaseModel
class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Represents a review with place_id, user_id, and text attributes.
    """
    
    # Public class attribute 'place_id', initialized to an empty string
    # Will store the ID of the Place the review is for
    place_id = ""
    
    # Public class attribute 'user_id', initialized to an empty string
    # Will store the ID of the User who wrote the review
    user_id = ""
    
    # Public class attribute 'text', initialized to an empty string
    # Represents the text content of the review
    text = ""
