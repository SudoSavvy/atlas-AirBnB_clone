from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity for Airbnb."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance."""
        super().__init__(*args, **kwargs)
