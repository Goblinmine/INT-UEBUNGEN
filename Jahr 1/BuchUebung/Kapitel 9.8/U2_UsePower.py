# Exercise:         Übungen zu Methoden, Prozeduren und Funktionen | Ü2
# Created by:       Jonas Millonig
# Creation date:    16. 03. 2023



def UsePower(number: float, n: float):
    output = 1
    for i in range(1, n +1):
        output *= number
    return output


print(UsePower(123, 4))