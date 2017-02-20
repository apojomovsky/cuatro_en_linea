from strategy import Strategy
import random

class RandomColumnStrategy(Strategy):

    def return_column(self, board):
        return random.choice(board.playable_positions())
