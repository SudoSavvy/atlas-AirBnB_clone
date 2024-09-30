import unittest
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_creation(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(isinstance(model.id, str))

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertIn(f"BaseModel.{model.id}", storage.all())

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in model_dict)

    def test_str(self):
        model = BaseModel()
        self.assertIn("[BaseModel]", str(model))

    def test_update_attributes(self):
        model = BaseModel()
        model.name = "Test"
        self.assertEqual(model.name, "Test")

if __name__ == '__main__':
    unittest.main()
