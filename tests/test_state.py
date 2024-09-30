import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_initialization(self):
        """Test that a State instance is created correctly."""
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """Test default attributes of State."""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
