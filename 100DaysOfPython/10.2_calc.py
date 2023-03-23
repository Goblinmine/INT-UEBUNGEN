# Exercise:         Day 10.2 | Calculator
# Created by:       Jonas Millonig
# Creation date:    22. 03. 2023

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(first_num, second_num):
    return first_num + second_num

def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, seconde_num):
    return first_num * seconde_num

def divide(first_num, second_num):
    return first_num / second_num


def main():
    print(logo)
    result = 0
    while True:
        if result == 0:
            firs_num = float(input("What's your fist number?: "))
        else:
            firs_num = result      
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        
        if(operation == '+'):
            result = add(firs_num, second_num)
        elif(operation == '-'):
            result = subtract(firs_num, second_num)
        elif(operation == '*'):
            result = multiply(firs_num, second_num)
        elif(operation == '/'):
            result = divide(firs_num, second_num)        
        
        print(f"{firs_num} {operation} {second_num} = {result}")
        
        
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") != 'y':
            result = 0
        
        
main()