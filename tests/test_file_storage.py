import unittest
import os
import sys
from models.file_storage import FileStorage  # Ensure this import is correct
from models.base_model import BaseModel  # Ensure this import is correct

# Add the models directory to the path if needed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../models')))
