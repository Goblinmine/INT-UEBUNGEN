# Exercise:         Blind Auction DIY
# Created by:       Jonas Millonig
# Creation date:    16. 03. 2023

from art import logo
import os
import math



def AddBidder(biddersDict: dict):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    biddersDict[name] = bid
    
    
def CalcWiner(biddersDict: dict):
    winnerKey = ""

    for bidder in biddersDict:
        if winnerKey == "":
            winnerKey = bidder
        
        if biddersDict[bidder] > biddersDict[winnerKey]:
            winnerKey = bidder
            
    return winnerKey, biddersDict[winnerKey]

def main():
    biddersDict = {}
    while True:
        os.system('cls')
        print(logo)
        print("Welcome to the secret auction program.")
        AddBidder(biddersDict)
        if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() != "yes":
            winner = CalcWiner(biddersDict)
            print(f"The winner is {winner[0]} with a bid of ${winner[1]}")
            break


main()