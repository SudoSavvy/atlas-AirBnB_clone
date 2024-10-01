from models.base_model import BaseModel  # Importing the BaseModel class for inheritance


class State(BaseModel):
    """Represents a state for Airbnb."""  # Documentation for the State class

    name = ""  # Public class attribute to store the name of the state

    def __init__(self, *args, **kwargs):
        """Initializes a State instance."""  # Documentation for the constructor
        super().__init__(*args, **kwargs)  # Calling the constructor of the parent class (BaseModel) to initialize inherited attributes
