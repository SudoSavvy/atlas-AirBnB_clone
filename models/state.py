#!/usr/bin/python3
# Importing the BaseModel class from the base_model module
from models.base_model import BaseModel

# Defining the State class, which inherits from BaseModel
class State(BaseModel):
    """
    State class that inherits from BaseModel.
    Represents a state with a name attribute.
    """
    
    # Public class attribute 'name', initialized to an empty string
    name = ""
