# Exercise:         Day 2.2 | BMI Calculator
# Created by:       Jonas Millonig
# Creation date:    

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

output = float(weight) / (float(height) * float(height))

#print(str(weight) + " / (" + str(height) + " x " + str(height) + ") = " + str(output))
print(int(output))