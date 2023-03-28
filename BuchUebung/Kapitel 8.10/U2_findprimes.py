# Exercise:         Kapitel 8.10 | Übung 2 Tupel und Listen
# Created by:       Jonas Millonig
# Creation date:    27. 03. 2023


user_input = int(input("Pick a number to count to: "))
numbers = [number for number in range(1, user_input + 1)]

for i in numbers: numbers = [number for number in numbers if not (i > 1 and number > i and number % i == 0)]

# for i in numbers: numbers = [0 if i > 1 and number > i and number % i == 0 else number for number in numbers]
# while numbers.__contains__(0): numbers.remove(0)

print(numbers)