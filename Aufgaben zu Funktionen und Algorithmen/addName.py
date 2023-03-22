# Exercise:         Add Name
# Created by:       Goblinmine
# Creation date:    20. 03. 2023

def add_name():
    output = []
    
    while True:
        name = input("Input name to add pls: ")
        if name == "":
            break
        output.append(name)
        
    return output


print(add_name())