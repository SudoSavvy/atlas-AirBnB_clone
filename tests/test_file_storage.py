import unittest
import os
import sys

# Add the models directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))

from file_storage import FileStorage  # Ensure correct import
from base_model import BaseModel  # Ensure correct import

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    # Your test methods go here...
