# Exercise:         Day 5.4 | FizzBuzz
# Created by:       Jonas Millonig
# Creation date: 
   
#Write your code below this row 👇


for val in range(1, 101):
    if val % 15 == 0:
        print("FizzBuzz")
    elif val % 5 == 0:
        print("Buzz")
    elif val % 3 == 0:
        print("Fizz")
    else:
        print(val)
