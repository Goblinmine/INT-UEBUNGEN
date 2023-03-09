import random
from hangman_art import logo, stages
from hangman_words import word_list

# def OutputWord(word: list):
#     output = ""
#     for letter in word:
#         output += f" {letter} "
#     return output

print(logo)
ranWord = random.choice(word_list)
lives = len(stages) -1

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
            
    # word output
    outputStr = ""
    for letter in output:
        outputStr += f" {letter} " 
    print(outputStr)
    
    # won game
    if not letter.__contains__("_"):
        print(f"You won the game!")
        exit()
    
    print(stages[lives])
    
    if lives == 0:
        print(f"lost! the word was {ranWord}")
        exit()

