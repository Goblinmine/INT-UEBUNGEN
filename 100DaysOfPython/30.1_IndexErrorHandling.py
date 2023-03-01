# Exercise:         Day 30.1 | IndexError Handling
# Created by:       Jonas Millonig
# Creation date:    01.03.2023

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

make_pie(4)