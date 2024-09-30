import unittest
import os
from models.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the FileStorage instance before each test."""
        self.fs = FileStorage()
        self.bm = BaseModel()
        self.fs.new(self.bm)
        self.fs.save()

    def tearDown(self):
        """Remove the JSON file after each test."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_initialization(self):
        """Test that FileStorage initializes correctly."""
        self.assertIsInstance(self.fs, FileStorage)

    def test_all_method(self):
        """Test the all method of FileStorage."""
        self.assertEqual(self.fs.all(), {f'BaseModel.{self.bm.id}': self.bm})

    def test_new_method(self):
        """Test the new method of FileStorage."""
        self.assertIn(f'BaseModel.{self.bm.id}', self.fs.all())

    def test_save_method(self):
        """Test the save method of FileStorage."""
        self.fs.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        """Test the reload method of FileStorage."""
        self.fs.save()
        self.fs.reload()
        self.assertIn(f'BaseModel.{self.bm.id}', self.fs.all())


if __name__ == '__main__':
    unittest.main()
