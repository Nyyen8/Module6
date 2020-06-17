"""
Program: test_valid_input_functions.py
Author: Paul Elsea
Last Modified: 06/17/2020

Program to test score_input function
"""

import unittest
from more_functions import inner_functions_assignment as inner


class MyTestCase(unittest.TestCase):

    def test_measurements_rectangle(self):
        self.assertEqual(inner.measurements([2.1, 3.4]), 'Perimeter = 11.0  Area = 7.14')

    def test_measurements_square(self):
        self.assertEqual(inner.measurements([3.5]), 'Perimeter = 14.0  Area = 12.25')


if __name__ == '__main__':
    unittest.main()
