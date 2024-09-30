import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_initialization(self):
        """Test that a Review instance is created correctly."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """Test default attributes of Review."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
