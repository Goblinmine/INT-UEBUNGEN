# Exercise:         Day 10.2 | Black Jack
# Created by:       Jonas Millonig
# Creation date:    23. 03. 2023

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def get_emty_table():
    return {
        "dealer":{
            "points": 0,
            "cards": []
        },
        "player":{
            "points": 0,
            "cards": []
        }
    }


def give_random_cards(guy: dict[str, any], how_many: int = 1):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(how_many):
        guy["cards"].append(cards[random.randint(0, len(cards) - 1)])
        
def show_cards_on_table(cards_on_table: dict[str, dict[str, any]], final = False):
    if final:
        print(f"  Your final hand: {cards_on_table['player']['cards']}, final score: {cards_on_table['player']['points']}")
        print(f"  Computer's final hand: {cards_on_table['dealer']['cards']}, final score: {cards_on_table['dealer']['points']}")
    else:
        print(f"  Your cards: {cards_on_table['player']['cards']}, current score: {cards_on_table['player']['points']}")
        print(f"  Computer's first card: {cards_on_table['dealer']['cards'][0]}")
    
def calc_ace(guy: dict[str, any]):
    guy["points"] = sum(guy["cards"])
    if guy["points"] > 21:
        for card in guy["cards"]:
            if card == 11 and guy["points"] > 21:
                first_index_11 = guy["cards"].index(11)
                guy["cards"][first_index_11] = 1
                guy["points"] = sum(guy["cards"])

def calc_dealer(dealer: dict[str, any]):
    dealer["points"] = sum(dealer["cards"])
   
    while dealer["points"] < 17:    
        give_random_cards(dealer)
        calc_ace(dealer)
        dealer["points"] = sum(dealer["cards"])
        
def smoke_on_the_water(cards_on_table: dict[str, dict[str, any]]):
    player_points = cards_on_table["player"]["points"]
    dealer_points = cards_on_table["dealer"]["points"]
    output = ""
    
    if player_points == dealer_points:
        print("You got the same points as the Dealer. Draw")
        return
    
    
    if player_points > 21:
        output += "You went over. "
        if player_points < dealer_points:
            output += "But you still won"
        else:
            output += "You lose"
            
    
    elif dealer_points > 21:
        output += "The Dealer went over. You won"
        
    elif dealer_points > player_points:
        output += "The Dealer has a higher score. You lose"
    else:
        output += "You got the higher score. You win"
            
    
    print(output)


def main():
    # main loop. end of loop when lost or won
    while True:
        # draw logo and first pick.
        print(logo)
        cards_on_table = get_emty_table()
        
        give_random_cards(cards_on_table["dealer"], 2)
        give_random_cards(cards_on_table["player"], 2)
        calc_ace(cards_on_table["player"])

        # check
        gameover = True if cards_on_table["player"]["points"] > 21 else False
        
        if not gameover:
        
            show_cards_on_table(cards_on_table)
            
            # mid game loop. get out of it if check. or if player selects stand
            while input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
                give_random_cards(cards_on_table["player"])
                calc_ace(cards_on_table["player"])
                
                if cards_on_table["player"]["points"] > 21:
                    break
                
                show_cards_on_table(cards_on_table)
        
        # calc points and winner. show end screen.
        calc_dealer(cards_on_table["dealer"])
        show_cards_on_table(cards_on_table, final=True)
        smoke_on_the_water(cards_on_table)
    
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower() != 'y':
            break
    
main()