from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city for Airbnb."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a City instance."""
        super().__init__(*args, **kwargs)
