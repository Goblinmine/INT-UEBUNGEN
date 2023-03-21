def AddName():
    output = []
    
    while True:
        name = input("Input name to add pls: ")
        if name == "":
            break
        output.append(name)
        
    return output


print(AddName())