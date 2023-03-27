# Exercise:         Kapitel 8.10 | Übung 1 Tupel und Listen
# Created by:       Jonas Millonig
# Creation date:    27. 03. 2023

# n-1

numbers = (0, 10, 12, 4, 7, 20, 21, 13)

user_input = int(input("Search value: "))
if numbers.__contains__(user_input):
    print(f"The index for that value is: {numbers.index(user_input)}")
else:
    print(f"{user_input} not in numbers tupel!")
