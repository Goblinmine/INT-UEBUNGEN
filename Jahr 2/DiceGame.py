# Exercise:         Dice Game
# Created by:       Jonas Millonig
# Creation date:    11. 09. 2023


import random

class Player:
    def __init__(self, name:str) -> None:
        self.name: str = name
        self.points: int = 0
        self.diceRounds: int = 0
        self.__data: list[list[int]] = []
        
    def Play(self, pointsToWin: int, diceAmount: int) -> None:
        """Plays rounds until the points to win is reached. 1 gives you 100 points, 6 gives you 60 points and the rest give nothing.

        Args:
            pointsToWin (int): points needet to win
            diceAmount (int): how many dice are thrown on each dice throw
        """
        self.__diceAmount = diceAmount
        while self.points < pointsToWin:
            self.points += self.__rollTheDice(self.__diceAmount)
            self.diceRounds += 1
            
    def ResetPoints(self) -> None:
        """Resets players points and diceRounds to start a new game.
        """
        self.points = 0
        self.diceRounds = 0
        self.__data = []
        
    def __rollTheDice(self, diceAmount: int) -> int:
        """Rolles the dice and calculates the points you are getting

        Args:
            diceAmount (int): How many dice you are throwing on each throw

        Returns:
            int: The sum of the points you are getting
        """
        points: int = 0
        for x in range(diceAmount):
            dicePoints = 0
            result = random.randint(1,6)
            if result == 1:
                dicePoints = 100
            elif result == 6:
                dicePoints = 60
            self.__data.append([result, dicePoints])
            points += dicePoints
        return points

    def __str__(self) -> str:
        return f'Name: {self.name}, points: {self.points}, rounds: {self.diceRounds}'

    def GameToStr(self) -> str:
        """Takes it's hole games data and formats it into a readable string

        Returns:
            str: Readable string of game data
        """
        # output = ''
        # width = 15
        # # go through rows
        # for y in range(self.diceRounds):
        #     # go through coloums
        #     for x in range(5):
        #       output += str(y+1).center()
            
    
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
        print(player.GameToStr())
        
main()