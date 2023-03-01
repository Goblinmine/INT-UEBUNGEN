# Exercise:         Day 3.2 | BMI 2.0
# Created by:       Jonas Millonig
# Creation date:    

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height * height)
bmiText = ""

if bmi < 18.5 :
    bmiText = "you are underweight."
elif bmi < 25 :
    bmiText = "you have a normal weight."
elif bmi < 30 :
    bmiText = "you are slightly overweight."
elif bmi < 35 :
    bmiText = "you are obese."
else :
    bmiText = "you are clinically obese."


print('Your BMI is ' + str(int(round(bmi, 0))) + ', ' + bmiText)