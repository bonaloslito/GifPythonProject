import unittest
import math
from unexpected import get_sqrt, divide


class TestUnexpeccted(unittest.TestCase):
    def test_get_sqrt(self):
        self.assertEqual(get_sqrt(144), 12)

        with self.assertRaises(TypeError):
            self.assertIn(144, -12)

    def test_divide(self):
        result = divide(144, 12)
        self.assertEqual(result, 12)

        with self.assertRaises(ZeroDivisionError):
            self.assertIn(144, 0)

