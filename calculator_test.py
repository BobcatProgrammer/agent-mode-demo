import unittest
from calculator import _add, _subtract, _multiply, _divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(_add(2, 3), 5)
        self.assertEqual(_add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(_subtract(5, 3), 2)
        self.assertEqual(_subtract(0, 4), -4)

    def test_multiply(self):
        self.assertEqual(_multiply(2, 3), 6)
        self.assertEqual(_multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(_divide(8, 2), 4)
        self.assertAlmostEqual(_divide(7, 3.5), 2)
        with self.assertRaises(ZeroDivisionError):
            _divide(5, 0)

if __name__ == "__main__":
    unittest.main()
