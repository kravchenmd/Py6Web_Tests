import unittest
from src.example.ops import add, sub, mul, div, async_add


class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class"""
        print("Set up class (before all tests)")

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down class"""
        print("Tear down class (after all tests)")

    def setUp(self) -> None:
        """Set up for each test"""
        # print("Set up")

    def tearDown(self) -> None:
        """Tear down for each test"""
        # print("Tear down")

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


class TestAsyncExample(unittest.IsolatedAsyncioTestCase):

    async def test_async_add(self):
        result = await async_add(2, 3)
        self.assertEqual(5, result)
