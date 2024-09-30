import unittest
from models.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_initialization(self):
        """Test initialization of FileStorage"""
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

# Add more tests as necessary

if __name__ == '__main__':
    unittest.main()
