# Jonas Millonig
# 08. 03. 2023
# 7 Kontrollstrukturen | Übung 2:  Geschachtelte Verzweigung

try:
    name = input("Name: ")
    sex = input("sex [m/f]: ")
    currentHour = int(input("Current timte? [0-24]: "))
except Exception:
    print("Input Error!")
    exit()
    
output = ""

if currentHour <= 9:
    output += "Guten Morgen"
elif currentHour <= 17:
    output += "Guten Tag"
else:
    output += "Guten Abend"
    
if sex == "m":
    output += " Herr "
elif sex == "f":
    output += " Frau "
    
    
print(output + name)