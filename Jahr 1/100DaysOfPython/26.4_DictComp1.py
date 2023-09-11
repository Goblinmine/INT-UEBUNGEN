# Exercise:         Day 26.4 | Dictionary Comprehension 1
# Created by:       Goblinmine
# Creation date:    

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {x:len(x) for x in sentence.split(' ')}



print(result)

