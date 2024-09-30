import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_initialization(self):
        """Test that a User instance is created correctly."""
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """Test default attributes of User."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
