# Exercise:         Übungen zu Methoden, Prozeduren und Funktionen | Ü2
# Created by:       Jonas Millonig
# Creation date:    16. 03. 2023

def FindMin(a: int, b: int, c: int):
    min = a
    for value in (a, b, c):
        if value < min:
            min = value
    return min
        
        
print(FindMin(123, 3, 4))