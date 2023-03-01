# Exercise:         Day 3.3 | Leap Year
# Created by:       Jonas Millonig
# Creation date:    

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leapYear = "Not leap year."

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leapYear = "Leap year."
    else :
        leapYear = "Leap year."

print(leapYear)
