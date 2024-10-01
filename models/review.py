from models.base_model import BaseModel  # Importing the BaseModel class for inheritance


class Review(BaseModel):
    """Represents a review for Airbnb."""  # Documentation for the Review class

    place_id = ""  # Public class attribute to store the ID of the place being reviewed
    user_id = ""  # Public class attribute to store the ID of the user who made the review
    text = ""  # Public class attribute to store the text of the review

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance."""  # Documentation for the constructor
        super().__init__(*args, **kwargs)  # Calling the constructor of the parent class (BaseModel) to initialize inherited attributes
