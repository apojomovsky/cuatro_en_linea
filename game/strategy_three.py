from game.strategy import Strategy
from game.gameboard import GameBoard

class StrategyThree(Strategy):
    """Look for the column that is closest to win in a vertical
       line for a given color, as long as a four-in-a-row could be completed
    """

    def _get_column_closest_to_win(self, board):
        current_max = [0,0]
        for column_index in range(GameBoard.COLUMNSCOUNT, 0, -1):
            current_column_count = board.count_same_color_on_top(column_index, self._color)
            current_free_entries = board.count_free_entries_on_column(column_index)
            if current_column_count > current_max[1] and current_column_count + current_free_entries >= 4:
                current_max[0] = column_index
                current_max[1] = current_column_count
        if current_max[1] > 0:
            return current_max[0]
        else:
            return 1

    def return_column(self, board):
        return self._get_column_closest_to_win(board)
