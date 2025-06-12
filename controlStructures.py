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
       return True
    else:
        return False

def displayMaximumNumber():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    if (num1 >= num2 and num1 >= num3):
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3

def isPrime():
    num = int(input("Enter a number: "))
    if (num <= 1):
        return False
    elif (num == 2 or num == 3 or num == 5 or num == 7):
        return False
    elif (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or  num % 7):
        return False
    else:
       return True

def fibonacciNumbers():
    n = int(input("Enter the number of Fibonacci numbers to print: "))
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    print(sequence[:n])
    
def calculateNewSalary(current_salary, job_level):
    if (job_level == 3):
        hike_percentage = 0.15
    elif (job_level == 4):
        hike_percentage = 0.07
    elif (job_level == 5):
        hike_percentage = 0.05
    else:
        hike_percentage = 0.0
    new_salary = current_salary + (current_salary * hike_percentage)
    return new_salary