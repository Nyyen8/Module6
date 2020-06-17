"""
Program: hourly_employee_input.py
Author: Paul Elsea
Last Modified: 06/16/2020

Program to accept user input for name, hours worked, and payrate. Results are printed.
"""

'''Function to accept user input for age and check it for a minimum amount'''
def get_hours():
    while True:
        try:
            hours = int(input("Please enter your hours worked: "))
        except ValueError:
            print("Invalid hours. Please use only whole numbers")
            continue

        if hours <= 0:
            print("Please enter hours of at least 1")
            continue
        else:
            break
    return hours

'''Function to accept user input for hourly pay and check it for a minimum amount'''
def get_pay():
    while True:
        try:
            pay = float(input("Please enter your hourly pay: "))
        except ValueError:
            print("Invalid pay. Please use only numbers")
            continue

        if pay <= 0:
            print("Please enter an pay of at least 1.00")
            continue
        else:
            break
    return pay

'''Function to accept user input for name, and call the valid_name_check func to check the input'''
def get_name():
    while True:
        name = input("Please enter your name: ")
        valid_result = valid_name_check(name)

        if valid_result == False:
            print("Please enter only first, or first and last names using only alphabetic characters and one space")
            continue
        else:
            break
    return name

'''Function to verify that input name uses only alphabetic characters'''
def valid_name_check(input_string):
    result = input_string.replace(" ", "").isalpha()
    return result

'''Method calls get_name(), get_hours(), and get_pay(). All results are saved as variables that are
then returned as a string'''
def hourly_employee_input():
    user_name = get_name()
    user_hours = get_hours()
    user_pay = get_pay()
    output_string = str(user_name + ' makes $' + str(round(user_pay, 2)) + ' an hour. Their weekly pay is ' + str(weekly_pay(user_hours, user_pay)))
    return output_string

'''This takes in hourly pay and hours worked and returns weekly pay
:input_hours: hours worker worked this week
:input_payrate: hourly payrate of employee
:returns: returns input_hours multiplied by input_payrate'''
def weekly_pay(input_hours, input_payrate):
    weekly_pay = input_hours * input_payrate
    return weekly_pay

if __name__ == '__main__':
    try:
        print(hourly_employee_input())
    except ValueError as err:
        print("Someone did something dumb so I'm gonna crash. Peace.")

'''Main method that calls hourly_employee_input()'''