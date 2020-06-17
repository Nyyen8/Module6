"""
Program: inner_functions_assignment.py
Author: Paul Elsea
Last Modified: 06/17/2020

Program to demonstrate inner functions
"""

'''This takes in an input list, calls perimeter() and area(), then prints final string.
:a_list: input list of 1 or 2 numbers
:returns: Perimeter and area in a string'''
def measurements(a_list):

    '''This takes a list and returns perimeter.
    :a_list: input list of 1 or 2 numbers
    :returns: Returns perimeter'''
    def perimeter(a_list):
        perimeter_result = 0
        if len(a_list) == 1:
            perimeter_result = a_list[0] * 4
        else:
            for side in a_list:
                perimeter_result += side * 2
        return perimeter_result

    '''This takes a list and returns area.
    :a_list: input list of 1 or 2 numbers
    :returns: Returns area'''
    def area(a_list):
        if len(a_list) == 1:
            area_result = a_list[0] * a_list[0]
        elif len(a_list) == 2:
            sideA = a_list[0]
            sideB = a_list[1]
            area_result = sideA * sideB
        return area_result

    return('Perimeter = ' + str(perimeter(a_list)) + '  Area = ' + str(area(a_list)))

if __name__ == '__main__':
    print(measurements([1,2]))