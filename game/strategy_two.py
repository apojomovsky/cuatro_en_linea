from game.strategy import Strategy

class StrategyTwo(Strategy):
    def return_column(self, board):
        return board.retrieve_emptiest_column()
