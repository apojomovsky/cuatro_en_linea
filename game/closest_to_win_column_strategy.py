from strategy import Strategy
from gameboard import GameBoard

class ClosestToWinColumnStrategy(Strategy):
    """Look for the column that is closest to win in a vertical
       line for a given color, as long as a four-in-a-row could be completed.
       Returns the first non full column otherwise.
    """
    def _can_complete_four(self, board, column_index, color):
        same_color_on_top = board.count_same_color_on_top(column_index, color)
        current_free_entries = board.count_free_entries_on_column(column_index)
        return same_color_on_top + current_free_entries >= 4

    def _get_closest_to_win_column(self, board, color):
        current_max_index = 0
        current_max_count = 0
        for column_index in range(1, GameBoard.COLUMNSCOUNT + 1):
            if self._can_complete_four(board, column_index, color):
                same_color_on_top = board.count_same_color_on_top(column_index, color)
                if same_color_on_top > current_max_count:
                    current_max_index = column_index
                    current_max_count = same_color_on_top
        if current_max_count > 0:
            return current_max_index
        return None

    def return_column(self, board, color):
        closest = self._get_closest_to_win_column(board, color)
        if closest:
            return closest
        return board.retrieve_first_non_full_column()
