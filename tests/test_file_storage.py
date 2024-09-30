import unittest
import os
from models.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def test_save_creates_file(self):
        self.storage.save()
        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))

    def test_reload_loads_objects(self):
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def test_all(self):
        self.storage.save()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)

    def test_new_object_storage(self):
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
