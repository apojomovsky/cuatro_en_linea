#!/usr/bin/env python
from gameboard import GameBoard
from gameboard import OutOfIndex
from gameboard import BoardIsFull
from multiprocessing import Pool

class Player(object):
    def __init__(self, color, strategy):
        self._color = color.upper()
        self._strategy = strategy
        self._pool = Pool(3)

    def prepare(self):
        self._strategy.prepare(self._color, self._pool)

    def color(self):
        return self._color

    def get_strategy_name(self):
        return type(self._strategy).__name__

    def is_winner(self, board):
        return board.is_game_over() and board.winner_color() == self._color

    def play(self, board):
        column_to_play = self._strategy.return_column(board.copy())
        if column_to_play is not None:
            if column_to_play in range(1, GameBoard.COLUMNSCOUNT + 1):
                board.put_chip(column_to_play, self._color)
            else:
                raise OutOfIndex
        else:
            raise BoardIsFull
