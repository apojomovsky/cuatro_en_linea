from game.strategy import Strategy

class StrategyOne(Strategy):
    def return_column(self, board):
        return board.retrieve_first_non_full_column()
