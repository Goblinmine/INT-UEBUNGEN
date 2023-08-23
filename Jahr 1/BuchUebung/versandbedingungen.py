# Jonas Millonig
# 27. 02. 2023
# Ü3.9 2

kosten = float(input("Einkaufspreis?\n"))
geschenk = False

if kosten <= 150:
    kosten += 8

if kosten >= 300:
    geschenk = True
    
    
print(f"Deine Kosten sind {kosten}€")
if geschenk:
    print("Du bekommst ein Gratisgeschenk!")