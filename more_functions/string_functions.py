"""
Program: string_functions.py
Author: Paul Elsea
Last Modified: 06/17/2020

Program to concatenate a string based off a chosen number of repetitions
"""
'''String to be repeated and Int for how many repetitions'''
class_string = 'Cuttlefish psychology '
repetitions = 3

'''This takes in an input string and a number of repetitions, 
concatenates the string for how ever many repetitions are input, 
then returns the resulting string
:string_input: string to be multiplied
:repetitions_input: number of times to multiply the string
:returns: returns multiplied input string'''
def multiply_string(string_input, repetitions_input):
    multiplied_string = ''
    while repetitions_input > 0:
        multiplied_string = multiplied_string + string_input
        repetitions_input -= 1
    return multiplied_string

if __name__ == '__main__':
    try:
        print(multiply_string(class_string, repetitions))
    except ValueError as err:
        print("Someone did something dumb so I'm gonna crash. Peace.")

'''Main method that calls multiply_string()'''