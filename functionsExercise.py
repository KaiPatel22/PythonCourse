'''
Exercise - 1
Write a Python function, find_square() that accepts an integer number n and returns the square of n. 
Invoke the function and display the square of the number. 

Exercise - 2
Write a Python function, find_sum() that accepts an integer n and returns the sum of first n numbers. 
Invoke the function and display the sum of first n numbers.
'''

def find_square(n):
    return n**2

def find_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(find_square(4))
print(find_sum(5))

'''
Write a Python function factorial(num) which returns the factorial of a given number.
Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome else returns false. Invoke the function and based on return value print the output.

Example: num=12321 output: Given number is a palindrome, num=12345 output: Given number is not a palindrome

Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments and returns True if the given pair of numbers are amicable numbers else return false. Invoke the function and based on return value print the numbers are amicable numbers or not.

num1 and num2 are said to be amicable numbers if sum of all the proper devisors (except num1 itself) of num1 is equal to num2 and sum of all the proper devisors of num2 (except num1 itself) is equal to num1.

Example: 220 and 284 are amicable numbers as

Proper devisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 whose sum is 284

Proper devisors of 284 are 1, 2, 4, 71, 142 whose sum is 220

Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments and returns value of the integer num rotated to the right by n positions. Assume both the numbers are unsigned. Invoke the function and print the return value.

Hint: use >> binary operator to shift the bits.

Example: num=60, n=2 result=15

Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns True if the number is strong number else false. Invoke the function and based on return value print the number is strong number or not.

A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.

Example:145 is strong number as

1!=1

4!=24

5!=120

Sum of all these is 145
'''

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
print(factorial(5))

def is_palindrome(num):
    str_num = str(num)
    isPalindrome = str_num == str_num[::-1]
    if isPalindrome:
        print("Given number is a palindrome")
        return True
    else:
        print("Given number is not a palindrome")
        return False

print(is_palindrome(12321))
print(is_palindrome(12345))

def findDivisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total

def check_amicable_numbers(num1, num2):
    sum1 = findDivisors(num1)
    sum2 = findDivisors(num2)
    if (sum1 == num2 and sum2 == num1):
        print(str(num1) + str(num2) + " are amicable numbers")
        return True
    else:
        print(str(num1) + str(num2) + " are not amicable numbers", sep=" ")
        return False
print(check_amicable_numbers(220, 284))