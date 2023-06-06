#!/usr/bin/env python3
import unittest
import factorial

class TestFactorial(unittest.TestCase):
    """
    Test factorial function
    """
    def test_factorial_5(self):
        self.assertEqual(factorial.factorial(5), 120)

    def test_factorial_3(self):
        self.assertEqual(factorial.factorial(3), 6)


if __name__ == '__main__':
    unittest.main()
