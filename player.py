import math
import random
# from game import *
import play

class Player:
    def __init__(self, letter):
        self.letter = letter


    def get_move(self, game):
        pass



class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = False
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    return ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')

        return val