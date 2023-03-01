# Exercise:         Day 26.5 | Dictionary Comprehension 2
# Created by:       Jonas Millonig
# Creation date:    

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:

weather_f = {x:round((y * 1.8 + 32), 1) for (x,y) in weather_c.items()}

print(weather_f)