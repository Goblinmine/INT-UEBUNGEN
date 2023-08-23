import math

MENU = {
    "espresso": {
        "name": "Caffee Espresso",
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "name": "Caffee Latte",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "name": "Caffee Cappuccino",
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    # "irish": {
    #     "ingredients": {
    #         "water": 250,
    #         "milk": 100,
    #         "coffee": 24,
    #     },
    #     "cost": 3.0,
    # }
}

machine = {
    "resources":{
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "errors":{
        "water": "Sorry there is not enoug water!",
        "milk": "Sorry there is not enoug milk!",
        "coffee": "Sorry there is not enoug coffee"
    },
    "money": 0
}


money_types = {
    "quarter":0.25,
    "dimes":0.1,
    "nickles":0.05,
    "pennies":0.01
}


def menu() -> tuple[bool, dict]:  
    coffee_types = ""
    for key in MENU:
        coffee_types += key
        if list(MENU)[-1] != key:
            coffee_types += '/'
    
    user_input = input(f"What would you like? ({coffee_types}): ").lower()
    try:
        coffee_type = MENU[user_input]
    except KeyError:
        # check if other command
        if user_input == "off":
            print("Shuting down machine!")
            exit()
        elif user_input == "report":
            show_report()
        
        # command not found
        if input(f'Input "{user_input}" not found! Do you want to try again? (y/n): ').lower() == 'y':
            return True, menu()
        else:
            return False, None
    return True, coffee_type

def make_coffee(coffee_type):
    # check resources   
    for key in machine["resources"]:
        if machine["resources"][key] - coffee_type["ingredients"][key] < 0:
            return machine["errors"][key]
        machine["resources"][key] -= coffee_type["ingredients"][key]
        

    
# print(resources) 
# make_coffee(MENU["latte"])
# print(resources)
    

def turn_mashine_off():
    exit()

def show_report():
    print(f"Water: {machine['resources']['water']}ml")
    print(f"Milk: {machine['resources']['milk']}ml")
    print(f"Coffee: {machine['resources']['coffee']}g")
    print(f"Money: ${machine['money']}")


# print(ask_coffee_type())

def get_money(needed: int):
    money_now = 0
    while money_now < needed:
        try:
            user_input = input("pls input some coins or refund (quarter/dime/nickle/pennie/refund): ")
            money_now += money_types[user_input]
            round(money_now, 2)
        except KeyError:
            print("Input Error!")
        print(f"${money_now} is in the machine. ${needed - money_now} still needed")
        
    if money_now > needed:
        print(f"Here is your change: {money_now - needed}")
        
    machine["money"] -= money_now
    return True


def main():
    while True:
        
        output = menu()
        
        if not output[0]:
            exit()
        
        picked_coffee = output[1]
        machine["money"] += get_money(picked_coffee["cost"])
        if get_money(picked_coffee["cost"]):
            make_coffee(picked_coffee)
            print(f"Here is your {picked_coffee['name']}. Enjoy!")
        
        
main()