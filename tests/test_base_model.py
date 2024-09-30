import unittest
import datetime  # Import datetime module
from models.base_model import BaseModel
from models.file_storage import FileStorage  # Ensure FileStorage is imported


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_initialization(self):
        """Test that a BaseModel instance is created correctly."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_id(self):
        """Test that each BaseModel instance has a unique id."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at(self):
        """Test that created_at is a datetime instance."""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test that updated_at is updated on save."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)


if __name__ == '__main__':
    unittest.main()
