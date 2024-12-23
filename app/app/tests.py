"""
    Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """
    Test the calc module.
    """

    def test_add_numbers(self):
        """Test adding two numbers together."""
        res = calc.add(5, 7)

        self.assertEqual(res, 12)

    def test_subtract_numbers(self):
        """Test subtract two numbers together."""
        res = calc.subtract(6, 6)

        self.assertEqual(res, 0)
