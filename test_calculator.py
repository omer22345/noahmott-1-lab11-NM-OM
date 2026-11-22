#https://github.com/noahmott-1/lab11-NM-OM.git
#Partner 1- Noah
#Partner 2- Omar

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(0,0), 0)
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(3,5), -2)
        self.assertEqual(subtract(0,0), 0)

    def test_multiply(self):
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-2,3), -6)
        self.assertEqual(mul(0,5), 0)

    def test_divide(self):
        self.assertEqual(div(2,10), 5)
        self.assertEqual(div(5,25), 5)
        self.assertEqual(div(-2,10), -5)


    def test_divide_by_zero(self): # 1 assertion
         with self.assertRaises(ZeroDivisionError):
             div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,8),3)
        self.assertEqual(logarithm(10,100),2)
        self.assertEqual(logarithm(3,9),2)
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,100)
    
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(-3,4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
