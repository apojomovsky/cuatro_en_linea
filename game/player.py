#!/usr/bin/env python
from game.gameboard import GameBoard
from game.gameboard import OutOfIndex
from game.gameboard import BoardIsFull

class Player(object):
    def __init__(self, color, strategy):
        self._color = color.lower()
        self._strategy = strategy

    def is_winner(self, board):
        return board.is_game_over() and board.winner_color() == self._color

    def play(self, board):
        column_to_play = self._strategy.return_column(board, self._color)
        if column_to_play is not None:
            if column_to_play in range(1, GameBoard.COLUMNSCOUNT + 1):
                board.put_chip(column_to_play, self._color)
            else:
                raise OutOfIndex
        else:
            raise BoardIsFull
