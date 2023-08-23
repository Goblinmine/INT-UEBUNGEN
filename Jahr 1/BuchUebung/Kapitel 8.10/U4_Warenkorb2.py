# Exercise:         Kapitel 8.10 | Übung 4 Dictinoaries
# Created by:       Jonas Millonig
# Creation date:    27. 03. 2023

warenkorb = {}


while True:
    product = input("Input product: ")
    count = int(input("How many?: "))
    warenkorb.update({product: count})
    
    user_input = input("Do you want to continue [c], to buy [b] or to cancel [any]: ")
    
    if user_input == 'b':
        print(f"You are buying {warenkorb}")
        break
    elif user_input == 'c':
        print(f"Things currently in warenkorb: {warenkorb}")
    else:
        break