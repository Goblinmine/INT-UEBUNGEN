# Exercise:         Day 30.1 | IndexError Handling
# Created by:       Jonas Millonig
# Creation date:    

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)