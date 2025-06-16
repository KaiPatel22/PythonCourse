'''
Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.
Example: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110

Write a Python function generate_fibonacci(n) to return a list of first n Fibonacci numbers.

Write a Python program to generate the next 15 leap years starting from a given year. 
Populate the leap years into a list and display the list.
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. 
Repetition of character has to be replaced by storing the length of that run.

Write a python function encode(message)  which performs the run length encoding for a given String and returns the run length encoded String. 
Provide different String values and test your program.
Example: message=AAAABBBBCCCCCCCC  output: 4A4B8C

Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
and use it to translate your Christmas wishes from English into Swedish. That is, write a Python function translate(b_dict,list_words) that accepts the bilingual dictionary and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words.
'''

def proper_divisors(num):
    properDivisors = []
    for i in range(1, num):
        if num % i == 0:
            properDivisors.append(i)
    return properDivisors

print(proper_divisors(220))

def generate_fibonacci(n):
    sequence = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return sequence[0]
    elif n == 2:
        return sequence
    else:
        for i in range(2, n):
            nextNum = sequence[i - 1] + sequence[i - 2]
            sequence.append(nextNum)
    return sequence

print(generate_fibonacci(10))

def generate_leap_years(startYear):
    leapYears = []
    currentYear = startYear
    isLeapYear = False
    while len(leapYears) < 15:
        if (currentYear % 4 == 0 and currentYear % 100 != 0) or (currentYear % 400 == 0):
            isLeapYear = True
        
        if isLeapYear:
            leapYears.append(currentYear)
            currentYear += 4
        else:
            currentYear += 1
    return leapYears

print(generate_leap_years(2021))

def encode(message):
    returnString = ""
    occruences = 1
    for i in range(1, len(message)):
        if (message[i] == message[i-1]):
            occruences += 1
        else:
            returnString += str(occruences) + message[i-1]
            occruences = 1
    returnString += str(occruences) + message[-1]
    return returnString

print(encode("AAAABBBBCCCCCCCC"))

def translate(b_dict, list_words):
    for i in range(len(list_words)):
        if list_words[i] in b_dict:
            list_words[i] = b_dict.get(list_words[i])
    return list_words

print(translate({"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}, ["merry", "year", "and", "new", "happy", "christmas"]))