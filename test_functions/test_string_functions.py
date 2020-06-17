import unittest
from more_functions import string_functions as strings


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual('PaulPaulPaul', strings.multiply_string())



if __name__ == '__main__':
    unittest.main()
