# Exercise:         Day 2.3 | Life in Wekks
# Created by:       Goblinmine
# Creation date:    

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

ageleft = 90 - int(age)

months = ageleft * 12
weeks = ageleft * 52
days = ageleft * 365


print(f'You have {days} days, {weeks} weeks, and {months} months left.')