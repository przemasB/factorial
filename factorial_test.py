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

    def test_factorial_1(self):
        self.assertEqual(factorial.factorial(1), 1)

    def test_factorial_2(self):
        self.assertEqual(factorial.factorial(2), 2)
        
    def test_factorial_4(self):
        self.assertEqual(factorial.factorial(4), 24)
        
    def test_factorial_4(self):
        self.assertEqual(factorial.factorial(4), 24)



if __name__ == '__main__':
    unittest.main()
