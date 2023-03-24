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
        print(type(guy["cards"]))
        print(guy["cards"])
        guy["cards"].append(cards[random.randint(0, len(cards) - 1)])
        
def show_cards_on_table(cards_on_table: dict[str, dict[str, any]], final = False):
    if final:
        print(f"Your final hand: {cards_on_table['player']['cards']}, final score: {cards_on_table['player']['points']}")
        print(f"Computer's final hand: {cards_on_table['dealer']['cards']}, final score: {cards_on_table['dealer']['points']}")
    else:
        print(f"Your cards: {cards_on_table['player']['cards']}, current score: {cards_on_table['player']['points']}")
        print(f"Computer's first card: {cards_on_table['dealer']['cards'][0]}")
    
def calc_ace(guy: dict[str, any]):
    # print(type(guy['cards']))
    # print(guy['cards'])
    guy["points"] = sum(guy["cards"])
    if guy["points"] > 21:
        for card in guy["cards"]:
            if card == 11 and guy["points"] > 21:
                first_index_11 = guy["cards"].index(11)
                guy["cards"][first_index_11] = 1
                guy["points"] = sum(guy["cards"])
    return guy





                
# # if dealer < 17
# def calc_points(cards_on_table: dict[str, list]):
#     dealer_points = 0
#     player_points = 0
#     for guy in cards_on_table:
#         if guy == "dealer":
#             dealer_points = sum(cards_on_table[guy])
            
#             if dealer_points < 17:    
#                 give_random_cards(cards_on_table[guy])
#                 dealer_points = sum(cards_on_table[guy])
            
#             if dealer_points > 21: # if dealer has 21 check if he has a 11 and make it to a 1
#                 for dealer_card in cards_on_table[guy]:
#                     if dealer_card == 11 and dealer_points > 21:
#                         cards_on_table[guy][cards_on_table[guy].index(dealer_card)] = 1 # find index of value and set it to 1
#                         dealer_points = sum(cards_on_table[guy])
#         else:
#             player_points = sum(cards_on_table[guy])
            
#     return dealer_points, player_points

def calc_dealer(dealers_cards: list):
    points = 0
    dealer_points = sum(dealers_cards)
   
    while dealer_points < 17:    
        give_random_cards(dealers_cards)
        # not sure about that
        # dealers_cards = over_21(dealers_cards)
        calc_ace(dealers_cards)
        dealer_points = sum(dealers_cards)
        
    
    
    # if dealer_points > 21: # if dealer has 21 check if he has a 11 and make it to a 1
    #     for card in dealers_cards:
    #         if card == 11 and dealer_points > 21:
    #             dealers_cards[dealers_cards.index(card)] = 1 # find index of value and set it to 1
    #             dealer_points = sum(dealers_cards)
                
    return points

def check_gameover(player_cards: list):
    calc_ace(player_cards)   
    if sum(player_cards) >= 21:
        return True
    
    return False
        
        
def show_end_screen(cards_on_table: dict[str, list]):

    # calc_winner(cards_on_table)
    points_dealer = sum(cards_on_table["dealer"])
    points_player = sum(cards_on_table["player"])
    
    calc_ace(cards_on_table["player"])   
    
    
    print(f"Your final hand: {cards_on_table['player']}, final score: {sum(cards_on_table['player'])}")
    print(f"Computer's final hand: {cards_on_table['dealer']}, final score: {sum(cards_on_table['dealer'])}")
    if points_player or points_dealer > 21:
        if points_player > points_dealer:
            print("You went over. You lose")
        elif points_player < points_dealer:
            print("You won")
        else:
            print("Draw")
        
    elif points_player > points_dealer:
        print("Computer got more points. You lose")
    elif points_player < points_dealer:
        print("You got more points. You win")
    else:
        print("draw")




# 4 cards are getting pulled. 2 for the play. they see it. 2 for dealer. player only sees 1


def main():
    # main loop. end of loop when lost or won
    while True:
        # draw logo and first pick.
        print(logo)
        cards_on_table = get_emty_table()
        
        give_random_cards(cards_on_table["dealer"], 2)
        give_random_cards(cards_on_table["player"], 2)
        calc_ace(cards_on_table["player"])
        
        show_cards_on_table(cards_on_table)
        
        # check 
        # mid game loop. get out of it if check. or if player selects stand
        while input("Do you want to take another card or stand? [c]ard / [s]and\n").lower() == 'c':
            give_random_cards(cards_on_table["player"])
            show_cards_on_table(cards_on_table)
        
        # calc points and winner. show end screen.
        show_cards_on_table(cards_on_table, final=True)
    
        if input("Want to try again? y / n\n") != 'y':
            break
        
        
        
    
    
    
    
    # while True:
    #     cards_on_table = get_emty_table()
    #     give_random_cards(cards_on_table["dealer"], 2)
    #     give_random_cards(cards_on_table["player"], 2)
    #     show_cards_on_table(cards_on_table)
        
    #     if check_gameover(cards_on_table["player"]):
    #         show_end_screen(cards_on_table)
    #         break
        
        
    #     while True:
    #         player_input = input("Do you want to take another card or stand? [c]ard / [s]and\n").lower()
    #         if player_input == 'c':
    #             # takes another card.
    #             give_random_cards(cards_on_table["player"])
    #             show_cards_on_table(cards_on_table)
    #             break
    #         elif player_input == 's':
    #             pass
    #             break
    #         else:
    #             print("wrong input. try again\n")
        
    #     if input("Want to try again? y / n\n") != 'y':
    #         break
        
        
    
main()


    
    
