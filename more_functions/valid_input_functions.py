"""
Program: valid_input_functions.py
Author: Paul Elsea
Last Modified: 06/17/2020

Program to concatenate a string based off test name and score
"""

'''This takes in an input string, integer, and a error message. There are default
values for the integer and error message.
:name: string test name
:score: integer score of test
:error_message: string that is printed if invalid input is received.
:returns: Test name and score as a string'''

def score_input(name, score = 0, error_message = 'Invalid test score, Please try again'):
    '''# return {test_name : test_score}'''
    try:
        output_score = int(score)
        if 0 > output_score  or output_score > 100:
            if output_score > 100:
                return('Score is above maximum. Please enter score between 0 and 100')
            else:
                return('Score is below minimum. Please enter score between 0 and 100')

        output_string = name + ' with a score of ' + str(output_score)
        return output_string

    except ValueError:
        return error_message


if __name__ == '__main__':
    try:
        test_name = input('Enter test name: ')
        test_score = int(input('Enter test score: '))
        print(score_input(test_name, test_score))

    except ValueError as err:
        print("Someone did something dumb so I'm gonna crash. Peace.")

'''Main method that calls hourly_employee_input()'''