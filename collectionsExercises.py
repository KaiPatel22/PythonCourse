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

'''
Write a python function, encrypt_sentence(msg) which accepts a message and encrypts it based on rules given below and returns the encrypted message.

Words at odd position -> Reverse It

Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

          Perform case sensitive string operations wherever necessary.

Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea
'''

def encode_message(msg):
    returnString = ""
    wordsInMsg = msg.split(" ")
    vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(wordsInMsg)):
        currentWord = wordsInMsg[i]
        if (i % 2 != 0):
            newWord = ""
            vowelSection = ""
            constantSection = ""
            for i in range(len(currentWord)):
                currentChar = currentWord[i]
                if (currentChar in vowelList):
                    vowelSection += currentChar
                else:
                    constantSection += currentChar
            newWord = constantSection + vowelSection
        else:
            newWord = currentWord[::-1]
        returnString += newWord + " "
    return returnString

print(encode_message("the sun rises in the east"))

'''
Write a Python program to find the number of characters present the given string.

Write a Python program to find the numbers of words present in the given sentence.
'''

def count_characters(message):
    numOfChars = 0
    for char in message:
        if char != " ":
            numOfChars += 1
    return numOfChars

print(count_characters("Hello World!"))

def count_words(sentence):
    words = sentence.split(" ")
    return len(words)

print(count_words("This is my sentence to check how many words there are."))

'''
Write a Python function words_count(sentence) to return a dictionary with the length of words as key and number words with such length as value.

Example: sentence=“I love python and it so easy to learn” sample output={1:1,4:2,5:1,3:1,2:3,6:1}
'''

def words_counts(sentence):
    wordsInSentence = sentence.split(" ")
    dictionary = {}
    for word in wordsInSentence:
        lengthOfWord = len(word)
        if lengthOfWord in dictionary:
            dictionary[lengthOfWord] += 1
        else:
            dictionary[lengthOfWord] = 1
    return dictionary

print(words_counts("I love python and it so easy to learn"))

'''
Write a Python function vowel_count(sentence) to return a dictionary with vowels, consonants, others as key and respective number of vowels, consonants, others characters as value.

Note: Do case insensitive operations

Example: sentence=“I love python and it so easy to learn”
sample output={“vowels”:12,”consonants”:17, “others”:8}
'''

def vowel_count(sentence):
    vowelList = ['a', 'e', 'i', 'o', 'u']
    constantsList = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    dictionary = {"vowels": 0, "consonants": 0, "others": 0}
    sentence = sentence.lower()
    for char in sentence:
        if char in vowelList:
            dictionary["vowels"] += 1
        elif char in constantsList:
            dictionary["consonants"] += 1
        else:
             dictionary["others"] += 1
    return dictionary

print(vowel_count("I love python and it so easy to learn"))
