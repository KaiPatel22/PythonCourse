'''
Given a list of numbers, write a Python function to return the list of prime numbers present in it.

Example: input:[7,9,11,13,15,20,23] output:[7,11,13,23]

Write a python function find_common_characters(msg1,msg2) to display all the common characters between given two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Example: msg1="I like Python", msg2="Java is a very popular language" output=lieyon

Write a python function, find_pairs_of_numbers(num_list,n) which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.

Example: num_list=[1, 2, 7, 4, 5, 6, 0, 3], n=6 output:3
num_list= [3, 4, 1, 8, 5, 9, 0, 6], n=9 output:4
'''

def isPrime(num):
    if (num <= 1):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def findPrimeNumbers(numList):
    primeNumbers = []
    for num in numList:
        if isPrime(num):
            primeNumbers.append(num)
    return primeNumbers

print(findPrimeNumbers([7, 9, 11, 13, 15, 20, 23]))

def find_common_characters(msg1, msg2):
    msg1 = msg1.replace(" ", "")
    msg2 = msg2.replace(" ", "")
    common_chars = set(msg1) & set(msg2)
    if common_chars:
        return ''.join(common_chars)
    else:
        return -1

print(find_common_characters("I like Python", "Java is a very popular language"))