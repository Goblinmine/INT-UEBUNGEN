# Exercise:         Day 4.4 | Rock Paper Scissors
# Created by:       Jonas Millonig
# Creation date:    
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
assciArt = [rock, paper, scissors]

keepPlaying = True

while keepPlaying:
    chosen = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if chosen >= 0 and chosen <= 2:
        print(assciArt[chosen])

        robot = random.randint(0, 2)
        print("Computer chose:\n" + assciArt[robot])

        if robot == chosen:
            print("Unentschiden")
        elif robot == 0 and chosen == 1:
            print("AI wins")
        elif robot == 0 and chosen == 2:
            print("You win")
        elif robot == 1 and chosen == 0:
            print("AI wins")
        elif robot == 1 and chosen == 2:
            print("You win")
        elif robot == 2 and chosen == 0:
            print("You win")
        elif robot == 2 and chosen == 1:
            print("AI wins")
    else:
        print("Wrong input!!")
    
    if input("Do you wann play again? Y/N\n").upper() != 'Y':
        keepPlaying = False
        
    

