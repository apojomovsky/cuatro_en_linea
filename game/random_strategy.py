from strategy import Strategy
import random

class RandomStrategy(Strategy):
    def return_column(self, board, color):
        while True:
            column_number = random.randint(1, 7)
            if board.is_valid_move(column_number):
                return column_number
