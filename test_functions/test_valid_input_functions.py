"""
Program: test_valid_input_functions.py
Author: Paul Elsea
Last Modified: 06/17/2020

Program to test score_input function
"""

import unittest
from more_functions import valid_input_functions as valid


class MyTestCase(unittest.TestCase):
    '''Test to ensure mandatory input works'''
    def test_score_input_test_name(self):
        test_results = 'test with a score of 0'
        self.assertEqual(test_results, valid.score_input('test'))

    '''Test to ensure score in range works'''
    def test_score_input_test_score_valid(self):
        test_results = 'test with a score of 50'
        self.assertEqual(test_results, valid.score_input('test', 50))

    '''Test to ensure proper response to score too low'''
    def test_score_input_test_score_below_range(self):
        test_results = 'Score is below minimum. Please enter score between 0 and 100'
        self.assertEqual(test_results, valid.score_input('test', -1))

    '''Test to ensure proper response to score too high'''
    def test_score_input_test_score_above_range(self):
        test_results = 'Score is above maximum. Please enter score between 0 and 100'
        self.assertEqual(test_results, valid.score_input('test', 101))

    '''Test to ensure proper response to invalid input type for score'''
    def test_score_input_non_numeric(self):
        test_results = 'Invalid test score, Please try again'
        self.assertEqual(test_results, valid.score_input('test', 'test'))

    '''Test to ensure third input returns correctly'''
    def test_score_input_invalid_message(self):
        test_results = 'test message'
        self.assertEqual(test_results, valid.score_input('test', 'test', 'test message'))

'''main method to invoke tests'''
if __name__ == '__main__':
    unittest.main()
