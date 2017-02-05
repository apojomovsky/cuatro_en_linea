from game.strategy import Strategy

class StrategyEmptiestColumn(Strategy):
    def return_column(self, board, color):
        return board.retrieve_emptiest_column()
