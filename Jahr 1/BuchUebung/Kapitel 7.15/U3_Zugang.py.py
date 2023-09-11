# Jonas Millonig
# 08. 03. 2023
# 7 Kontrollstrukturen | Übung 3: Benutzereingaben überprüfen


name = input("Bitte Namen eingeben: ")
password = input("Bitte Password eingeben: ")

if name == "gast" and password == "geheim":
    print("Zugang erlaubt")
else:
    print("Zugang verboten")