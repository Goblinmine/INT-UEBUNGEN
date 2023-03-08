# Jonas Millonig
# 08. 03. 2023
# 7 Kontrollstrukturen | Übung 6: Verzweigungen und Schleifen


letzterTagVorjahr = int(input("Was war der letzte tag im vorjahr? 1-7 \n"))
isLeapYear = int(input("War das letzte jahr ein Schaltjar? 0 / 1\n"))


if isLeapYear:
    daysInYear = 366
    daysPerMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else :
    daysInYear = 365
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

output = 0
dayCounter = letzterTagVorjahr


for days in reversed(daysPerMonth):                                             # goes 12 through that loop; start with dec.
    for day in reversed(range(1, days +1)):                                     # goes 31/30/29/28 days through; start with last day
        if day == 1:
            if dayCounter == 7:                                                 # if dayCounter == Sunday and 1st day in month          # day counter start at letzterTagVorjahr
                # print(f"day counter: {dayCounter}, days in that month: {days}")
                output += 1
                
        if dayCounter == 1:
            dayCounter = 7
        else: dayCounter -= 1
    
print(f"In diesm Jahr gab es {output} Monat(e) wo der 1. ein Sonntag war")