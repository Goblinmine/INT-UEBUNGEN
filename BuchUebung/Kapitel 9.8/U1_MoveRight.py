# Exercise:         Übungen zu Methoden, Prozeduren und Funktionen | Ü1
# Created by:       Jonas Millonig
# Creation date:    16. 03. 2023

import math

def Calc(radius: float):
    umfang = 2* math.pi * radius
    mantelFläche = 4* math.pi * radius * 2
    volumen = 4 / 3 * math.pi * radius * 3
    
    return umfang, mantelFläche, volumen

print(Calc(4))