# Exercise:         Day 1.2 | Debugging Practice
# Created by:       Jonas Millonig
# Creation date:    11. 09. 2023


import random

class Player:
    def __init__(self, name:str) -> None:
        self.name: str = name
        self.points: int = 0
        self.diceRounds: int = 0
        
    def Play(self, pointsToWin: int, diceAmount: int) -> None:
        """Plays rounds until the points to win is reached. 1 gives you 100 points, 6 gives you 60 points and the rest give nothing
        
        Args:
            pointsToWin (int): points needet to win
            diceAmount (int): how many dice are thrown on each dice throw.
        """
        while self.points < pointsToWin:
            self.points += self.__rollTheDice(diceAmount)
            self.diceRounds += 1
            
    def ResetPoints(self) -> None:
        self.points = 0
        self.diceRounds = 0
        
    def __rollTheDice(self, diceAmount: int) -> int:
        points: int = 0
        for x in range(diceAmount):
            result = random.randint(1,6)
            if result == 1:
                points += 100
            elif result == 6:
                points += 60
        return points

    def __str__(self) -> str:
        return f'Name: {self.name}, points: {self.points}, rounds: {self.diceRounds}'

def main() -> None:
    # Settings
    diceAmount = 3
    pointsToWin = 1000
    
    players: list[Player] = list()
        

    while 'y' in input('\n\nIs there another player that want to play? (Y/N)').lower():
        currentPlayer = Player(input('Player name: '))
        currentPlayer.Play(pointsToWin, diceAmount)
        players.append(currentPlayer)
        
      
    for player in players:
        print(player)
        
main()