#!/usr/bin/python3
# Importing the BaseModel class from the base_model module
from models.base_model import BaseModel

# Defining the Amenity class, which inherits from BaseModel
class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Represents an amenity with a name attribute.
    """
    
    # Public class attribute 'name', initialized to an empty string
    # Represents the name of the amenity
    name = ""
