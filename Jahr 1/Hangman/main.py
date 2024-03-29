# Jonas Millonig
# 09. 03. 2023
# Hangman DiY

import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
ranWord = random.choice(word_list)
lives = len(stages) -1

# debug
# print(ranWord)


output = []
for letter in ranWord:
    output.append('_')

while True:
    guessedLetter = input("Guess a letter: ")
    
    if not ranWord.__contains__(guessedLetter):
        print(f"You guessed {guessedLetter}, that's not in the word. You lose a life.")
        lives -= 1
    else:
        counter = 0
        for letter in ranWord:
            if letter == guessedLetter:
                output[counter] = letter
            counter += 1    
            
    outputStr = ""
    for letter in output:
        outputStr += f" {letter} " 
    print(outputStr)
    
    # won game
    if not output.__contains__("_"):
        print(f"You won the game!")
        exit()
    
    print(stages[lives])
    
    if lives == 0:
        print(f"lost! the word was {ranWord}")
        exit()

