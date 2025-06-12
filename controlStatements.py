'''
Write a Python program to check whether the given year is leap year or not.

Write a Python program to find and display the maximum of three given numbers.

Write a Python program to check the given number is prime number or not.

Write a Python program to print first n Fibonacci numbers.

An organization has decided to provide salary hike to its employees based on their job level. 
Employees can be in job levels 3 , 4 or 5. In case of invalid job level, consider hike percentage to be 0. 
Given the current salary and job level, write a Python program to find and display the new salary of an employee. 
'''

def isLeapYear():
    year = int(input("Enter a year: "))
    if year < 0:
        print("Invalid year")
        return
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       print(year, "is a leap year")
    else:
         print(year, "is not a leap year")

def displayMaximumNumber():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    if (num1 >= num2 and num1 >= num3):
        print("Maximum number is:", num1)
    elif (num2 >= num1 and num2 >= num3):
        print("Maximum number is:", num2)
    else:
        print("Maximum number is:", num3)
