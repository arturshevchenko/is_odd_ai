import unittest
from unittest.mock import patch

from is_odd import is_odd


class TestIsOdd(unittest.TestCase):

    def test_is_odd_true(self):
        """Test that is_odd returns True for odd numbers"""
        result = is_odd(5)
        self.assertTrue(result, "Expected True for an odd number")

    def test_is_odd_false(self):
        """Test that is_odd returns False for even numbers"""
        result = is_odd(4)
        self.assertFalse(result, "Expected False for an even number")

    def test_is_odd_negative_number(self):
        """Test that is_odd works with negative odd numbers"""
        result = is_odd(-3)
        self.assertTrue(result, "Expected True for a negative odd number")

    def test_is_even_negative_number(self):
        """Test that is_odd works with negative even numbers"""
        result = is_odd(-4)
        self.assertFalse(result, "Expected False for a negative even number")

    def test_is_value_error_raised(self):
        """Test that is_odd raises ValueError for invalid input"""
        with self.assertRaises(ValueError):
            is_odd("abc")

    def test_is_no_valid_response_from_openai_api(self):
        """Test that is_odd raises ValueError when no valid response from OpenAI API"""
        with patch('requests.post') as mock_post:
            mock_post.return_value.json.return_value = {"choices": []}
            with self.assertRaises(ValueError, msg="Expected ValueError when no valid response from OpenAI API"):
                is_odd(5)

