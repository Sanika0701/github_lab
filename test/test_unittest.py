import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.calculator import fun1, fun2, fun3, fun4, fun5

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)
        with self.assertRaises(ValueError):
            fun1("a", 2)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)
        with self.assertRaises(ValueError):
            fun2(5, "b")

    def test_fun3(self):
        self.assertEqual(fun3(4, 3), 12)
        with self.assertRaises(ValueError):
            fun3("x", 3)

    def test_fun4(self):
        self.assertEqual(fun4(1, 2, 3), 6)
        with self.assertRaises(ValueError):
            fun4(1, "two", 3)

    def test_fun5(self):
        self.assertEqual(fun5(2, 3), 8)
        with self.assertRaises(ValueError):
            fun5(2, "3")

if __name__ == "__main__":
    unittest.main()
