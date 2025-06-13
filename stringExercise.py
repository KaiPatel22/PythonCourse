'''
Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number where,

Consider AL1 as the value for airline

src and dest should be the first three characters of the source and destination cities.

number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, then return the list of all generated ticket numbers.
'''

def generateTicketNumber(numberOfPassengers, sourceCity, destinationCity):
    airline = "AL1"
    src = sourceCity[:3]
    dest = destinationCity[:3]
    num = 101
    ticketNumbers = []
    for i in range(numberOfPassengers):
        ticketNumber = f"{airline}:{src}:{dest}:{num}"
        ticketNumbers.append(ticketNumber)
        num += 1
    
    if len(ticketNumbers) < 5:
        return ticketNumbers
    else:
        return ticketNumbers[:5]

print(generateTicketNumber(10, "London", "Madrid"))
print(generateTicketNumber(3, "London", "Madrid"))
