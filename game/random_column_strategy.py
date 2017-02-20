from strategy import Strategy
import random

class RandomColumnStrategy(Strategy):
    def return_column(self, board, color):
        return random.choice(board.playable_positions())
