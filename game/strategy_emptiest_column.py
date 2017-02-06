from game.strategy import Strategy

class StrategyEmptiestColumn(Strategy):
    """This strategy simply looks for the column that have more empty spaces
       on top. In case there are more than one columns with the same amount
       of empty spaces, the strategy will chose the leftmost one. 
    """
    def return_column(self, board, color):
        return board.retrieve_emptiest_column()
