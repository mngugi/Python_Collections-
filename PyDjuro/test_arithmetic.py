#test_arithmetic.py

import arithmetic
import unittest

class TestArithmetic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(arithmetic.add(2, 6), 8)
        
    def test_subtration(self):
        self.assertEqual(arithmetic.subtract(10, 6), 4)
        
    def test_multiplication(self):
        self.assertEqual(arithmetic.multiply(1, 2), 2)
        
    def test_division(self):
        self.assertEqual(arithmetic.divide(60, 60), 1)    
        
if __name__ == '__main__':
    unittest.main()       
