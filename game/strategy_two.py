from game.strategy import Strategy
from game.gameboard import BoardIsFull

class StrategyTwo(Strategy):
    def return_column(self, board, color):
        return board.retrieve_emptiest_column()
