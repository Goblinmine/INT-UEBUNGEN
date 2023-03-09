# Exercise:         Day 5.5 | Password Generator
# Created by:       Jonas Millonig
# Creation date:    27. 02. 2023

import secrets

letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

output = ""
symArray = ['!', '@', '*', '&', '%', '$', '#', '§']

def RandLetter():
    ranLetter = secrets.randbelow(52)
    if ranLetter <= 25:
        return chr(ranLetter + 65)
    else:
        return chr(ranLetter + 71)
    
def RandSymbol():
    ranSymbol = secrets.randbelow(len(symArray))
    return symArray[ranSymbol]

def RandNumber():
    return str(secrets.randbelow(9))

for x in range(letters):
    output += RandLetter()
for x in range(symbols):
    output += RandSymbol()    
for x in range(numbers):
    output += RandNumber()

if input("Would you like to use the advanced version? Y/N ").upper() == 'Y':
    
    howMany = len(output)
    outputArray = list(output)
    output = ""
    for i in range(howMany):
        iSelected = secrets.randbelow(len(outputArray))
        output += outputArray[iSelected]
        outputArray.remove(outputArray[iSelected])
        
print(f"The Password is {output}")
