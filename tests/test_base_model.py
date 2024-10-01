import unittest
import os
import sys


# Add the models directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))

from base_model import BaseModel  # Ensure correct import
from file_storage import FileStorage  # Ensure correct import

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""
