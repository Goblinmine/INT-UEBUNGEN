# Exercise:         Kapitel 8.10 | Übung 2 Tupel und Listen
# Created by:       Jonas Millonig
# Creation date:    27. 03. 2023

# to create the list

# numbers = [number for number in range(1, 1001)]
numbers = []
while True:
    user_input = int(input("put in a number: "))
    numbers.append(user_input)
    if input("Wonna calc? y/n") != 'n':
        break

for i in numbers: numbers = [0 if i > 1 and number > i and number % i == 0 else number for number in numbers]
while numbers.__contains__(0): numbers.remove(0)

print(numbers)