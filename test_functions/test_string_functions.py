import unittest
from more_functions import string_functions as strings

'''Test that calls multiply_string method with test string and integer
test_string: a string to be repeated
test_repetitions: how many times to repeat the test_string
return: true/false assertion of whether return of function and expected result are the same'''
class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        test_string = 'Paul'
        test_repetitions = 3
        self.assertEqual('PaulPaulPaul', strings.multiply_string(test_string, test_repetitions))


'''Default main method call to invoke test'''
if __name__ == '__main__':
    unittest.main()
