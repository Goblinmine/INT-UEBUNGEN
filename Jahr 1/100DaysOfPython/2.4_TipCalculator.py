# Exercise:         Day 2.3 | Tip Calculator
# Created by:       Jonas Millonig
# Creation date:    

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
hole = input("What was the total bill? ")
pers = input("What percentage tip would you like to give? 10, 12, or 15? ")
howMany = input("How many people to split the bill? ")

output = "{:.2f}".format(round((float(hole) / int(howMany)) * ((int(pers) / 100) + 1), 2)) 

print(f"Each person should pay: ${output}")