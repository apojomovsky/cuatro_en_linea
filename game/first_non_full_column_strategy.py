from strategy import Strategy

class FirstNonFullColumnStrategy(Strategy):
    """This strategy simply looks for the first non full
       column by looking from left to right.
    """
    def return_column(self, board, color):
        return board.retrieve_first_non_full_column()
