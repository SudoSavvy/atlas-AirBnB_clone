# tests/test_file_storage.py
import unittest
from models.file_storage import FileStorage  # Ensure the import path is correct

class TestFileStorage(unittest.TestCase):
    def test_instance(self):
        """Test that FileStorage instance is created correctly"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

if __name__ == '__main__':
    unittest.main()
