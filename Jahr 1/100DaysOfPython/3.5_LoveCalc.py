# Exercise:         Day 3.5 | Love Calculator
# Created by:       Goblinmine
# Creation date:    

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


counterTen = 0
counterOne = 0
for char in name1.upper() + name2.upper():
    for val in "TRUE":
        if char == val:
            counterTen += 1
            
    for val in "LOVE":
        if char == val:
            counterOne += 1

score = counterTen * 10 + counterOne
#score = int(str(counterTen) + str(counterOne))

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) <= 50 and int(score) >= 40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")