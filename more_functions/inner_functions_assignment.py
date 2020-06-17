"""
Program: inner_functions_assignment.py
Author: Paul Elsea
Last Modified: 06/17/2020

Program to demonstrate inner functions
"""

'''This takes in an input string, integer, and a error message. There are default
values for the integer and error message.
:name: string test name
:score: integer score of test
:error_message: string that is printed if invalid input is received.
:returns: Test name and score as a string'''
def measurements(a_list):
    perim_result = 0.0
    area_result = 0.0

    def perimeter(a_list):
        perimeter_result = 0
        for side in a_list:
            perimeter_result += side * 2
        return perimeter_result

    def area(a_list):
        sideA = a_list[0]
        sideB = a_list[1]
        area_result = sideA * sideB
        return area_result

    return('Perimeter = ' + str(perimeter(a_list)) + '  Area = ' + str(area(a_list)))

if __name__ == '__main__':
    print(measurements([1,2]))