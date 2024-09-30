#!/usr/bin/python3
# Importing the BaseModel class from the base_model module
from models.base_model import BaseModel

# Defining the City class, which inherits from BaseModel
class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Represents a city with state_id and name attributes.
    """
    
    # Public class attribute 'state_id', initialized to an empty string
    # Will store the ID of the State the city belongs to
    state_id = ""
    
    # Public class attribute 'name', initialized to an empty string
    # Represents the name of the city
    name = ""
