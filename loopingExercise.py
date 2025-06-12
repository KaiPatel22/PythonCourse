'''
Write a Python program to find the sum of digits of a given number.

Example: Sum of digits of the number 123 will be 6

Note: Initialize the number with various values and test your program.

'''

num = input("Enter a number: ")
sum = 0
for digit in num:
    if digit.isdigit():
        sum += int(digit)
print(sum)