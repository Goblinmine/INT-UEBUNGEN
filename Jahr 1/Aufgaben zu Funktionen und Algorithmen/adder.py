# Exercise:         Adder
# Created by:       Jonas Millonig
# Creation date:    20. 03. 2023

def add_number():
    output = 0
    
    while True:
        toAdd = int(input("gib nummer ein: "))
        if toAdd == 0:
            break
        output += toAdd
    return output


print(f"The sum is: {add_number()}")

