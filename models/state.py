from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state for Airbnb."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a State instance."""
        super().__init__(*args, **kwargs)
