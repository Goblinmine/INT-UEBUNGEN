# Exercise:         Day 55.1 | Advanced Decorators
# Created by:       Jonas Millonig
# Creation date:    01.03.2023

# Create the logging_decorator() function 👇

def logging_decorator(function, *args):
    print(f"You called {function.__name__}{args}")
    print(f"It returned: {function(*args)}")

# Use the decorator 👇

def BMI_calc(weight: float, height: float):
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
        
    return 'Your BMI is ' + str(int(round(bmi, 0))) + ', ' + bmiText

logging_decorator(BMI_calc, 80, 1.70)