#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel: 
    """BaseModel defines all common attributes and methods for other classes."""

    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4()) 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()