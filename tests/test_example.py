import unittest
from src.example.ops import add, sub, mul, div, async_add


class TestExample(unittest.TestCase):

    def test_add(self):
        """Add function test"""
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        """Sub function test"""
        self.assertEqual(sub(2, 3), -1)

    def test_mul(self):
        """Sub function test"""
        self.assertEqual(mul(2, 3), 6)

    def test_div(self):
        """Sub function test"""
        self.assertAlmostEqual(div(2, 3), 0.66666666)
