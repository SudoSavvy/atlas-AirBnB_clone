import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        """Test initialization of BaseModel"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
    
    def test_to_dict(self):
        """Test to_dict method"""
        instance = BaseModel()
        dict_repr = instance.to_dict()
        self.assertIn("id", dict_repr)
        self.assertIn("created_at", dict_repr)
        self.assertIn("updated_at", dict_repr)

# Add more tests as necessary for other functionalities

if __name__ == '__main__':
    unittest.main()
