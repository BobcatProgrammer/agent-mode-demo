import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add.__wrapped__(2, 3), 5)
        self.assertEqual(add.__wrapped__(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract.__wrapped__(5, 3), 2)
        self.assertEqual(subtract.__wrapped__(0, 4), -4)

    def test_multiply(self):
        self.assertEqual(multiply.__wrapped__(2, 3), 6)
        self.assertEqual(multiply.__wrapped__(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(divide.__wrapped__(8, 2), 4)
        self.assertAlmostEqual(divide.__wrapped__(7, 3.5), 2)
        with self.assertRaises(ZeroDivisionError):
            divide.__wrapped__(5, 0)

if __name__ == "__main__":
    unittest.main()
