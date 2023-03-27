import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):
    pass

class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)
    def test_add_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)
    def test_add_positive_negative_numbers(self):
        self.assertEqual(multiply(2, -3), -6)

if __name__ == "__main__":
    unittest.main()