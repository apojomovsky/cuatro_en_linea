from gameboard import GameBoard
from gameboard import OutOfIndex
from gameboard import BoardIsFull

class Player(object):
    def __init__(self, color, strategy):
        self._color = color.upper()
        self._strategy = strategy

    def color(self):
        return self._color

    def is_winner(self, board):
        return board.is_game_over() and board.winner_color() == self._color

    def play(self, board):
        column_to_play = self._strategy.return_column(board.copy(), self._color)
        if column_to_play is not None:
            if column_to_play in range(1, GameBoard.COLUMNSCOUNT + 1):
                board.put_chip(column_to_play, self._color)
            else:
                raise OutOfIndex
        else:
            raise BoardIsFull
