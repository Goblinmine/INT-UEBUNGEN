# Exercise:         Day 3.4 | Pizza order Practice
# Created by:       Jonas Millonig
# Creation date:    

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


prize = 0

if size == "S" :
    prize = 15
elif size == "M" :
    prize = 20
elif size == "L" :
    prize = 25
else :
    raise Exception("Sorry, wrong input")

if add_pepperoni == "Y" and size == "S" :
    prize += 2
elif add_pepperoni == "Y" :
    prize += 3
elif add_pepperoni != "N" :
    raise Exception("Sorry, wrong input")

if extra_cheese == "Y" :
    prize += 1
elif extra_cheese != "N" :
    raise Exception("Sorry, wrong input")

print(f"Your final bill is: ${prize}")

