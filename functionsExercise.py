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