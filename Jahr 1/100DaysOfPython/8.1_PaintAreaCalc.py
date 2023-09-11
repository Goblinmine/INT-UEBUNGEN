# Exercise:         Day 8.1 | Paint Area Calculator
# Created by:       Jonas Millonig
# Creation date: 
   
# Write your code below this line 👇
import math

# (height * width) / coverage


def paint_calc(height, width, cover):
    output = math.ceil((height * width) / cover)
    print(f"You'll need {output} cans of paint.")
    

# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

