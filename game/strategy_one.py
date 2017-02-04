from strategy import Strategy

class StrategyOne(Strategy):
    def return_column(self, board, color):
        return board.retrieve_first_non_full_column()
