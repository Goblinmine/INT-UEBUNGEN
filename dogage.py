#input dogs name and age
name = input("What is your dog's name? ")
dog_age = int(input("What is your dog's age? "))

#calc age in human years (age * 7)
human_age = dog_age * 7

#print dog name + human age
print(f"Your dog {name} is {human_age} years old in human years")