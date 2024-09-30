# tests/test_file_storage.py
import unittest
from models.file_storage import FileStorage  # Ensure this import is correct

class TestFileStorage(unittest.TestCase):
    def test_initialization(self):
        """Test that FileStorage initializes correctly."""
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_all_method(self):
        """Test the all method of FileStorage."""
        fs = FileStorage()
        self.assertEqual(fs.all(), {})

if __name__ == '__main__':
    unittest.main()
