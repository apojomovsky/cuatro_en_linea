from strategy import Strategy

class StrategyTwo(Strategy):
    def return_column(self, board, color):
        return board.retrieve_emptiest_column()
