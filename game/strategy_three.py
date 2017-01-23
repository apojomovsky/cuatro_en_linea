from game.strategy import Strategy
from game.gameboard import GameBoard

class StrategyThree(Strategy):
    """Look for the column that is closest to win in a vertical
       line for a given color, as long as a four-in-a-row could be completed.
       Returns first non full column otherwise
    """
    def _can_complete_four(self, board, column_index, color):
        same_color_on_top = board.count_same_color_on_top(column_index, color)
        current_free_entries = board.count_free_entries_on_column(column_index)
        return same_color_on_top + current_free_entries >= 4

    def _get_column_closest_to_win(self, board, color):
        current_max = [0, 0]
        for column_index in range(1, GameBoard.COLUMNSCOUNT + 1):
            if self._can_complete_four(board, column_index, color):
                same_color_on_top = board.count_same_color_on_top(column_index, color)
                if same_color_on_top > current_max[1]:
                    current_max[0] = column_index
                    current_max[1] = same_color_on_top
        if current_max[1] > 0:
            return current_max[0]
        return False

    def return_column(self, board, color):
        closest = self._get_column_closest_to_win(board, color)
        if closest:
            return closest
        return board.retrieve_first_non_full_column()
