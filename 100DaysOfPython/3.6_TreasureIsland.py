# Exercise:         Day 3.5 | Treasure Island
# Created by:       Jonas Millonig
# Creation date:    

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

def GameOver(msg = ''):
    print("\n-------------------------\n")
    if msg != '': print(msg)
    print("Game over!")
    print("\n-------------------------\n")
    exit()
    
def TookWrongStep(msg = "", right = ''):
    print("\n-------------------------\n")
    return input(msg + "\n").upper() != right
    

if TookWrongStep('You\'re at a crossroad. Where do you want to go? Type "L" or "R" ', 'L'):
    GameOver("You fell into hole")
if TookWrongStep('You\'ve come to a lake. There is an island in the middle of the lake. Type "W" to wait for a boat. Type "S" to swim across. ', 'W'):
    GameOver("You get attacked by an angry trout. ")

print("\n-------------------------\n")
lastInput = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? Type "R", "Y" or "B" \n').upper()

if lastInput != 'Y':
    if lastInput == 'R':
        GameOver('It\'s a room full of fire.')
    elif lastInput == 'B':
        GameOver("You enter a room of beasts.")
    GameOver("You chose a door that doesn't exist.")

print("\n-------------------------\n")
print("You found the treasure! You Win!")
print("\n-------------------------\n")