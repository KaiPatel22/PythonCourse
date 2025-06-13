'''
Given a list of integer values, write a Python program to check whether 
the list contains the same number in adjacent positions. 
Display the count of such adjacent occurrences.
'''

def countAdjacentOccurences(numList):
    count = 0
    for i in range(1, len(numList)):
        if numList[i] == numList[i - 1]:
            count += 1
    return count

print(countAdjacentOccurences([1,1,5,100,-20,-20,6,0,0]))