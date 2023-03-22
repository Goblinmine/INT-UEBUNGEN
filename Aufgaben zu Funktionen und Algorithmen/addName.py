# Exercise:         Add Name
# Created by:       Jonas Millonig
# Creation date:    20. 03. 2023

def AddName():
    output = []
    
    while True:
        name = input("Input name to add pls: ")
        if name == "":
            break
        output.append(name)
        
    return output


print(AddName())