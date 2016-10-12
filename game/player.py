#!/usr/bin/env python
from game.gameboard import GameBoard

class Player(object):
    def __init__(self, color):
        self._color = color.lower()

    def color(self):
        return self._color

    def is_winner(self, board):
        if board.game_over:
            if board.winner_color() == self._color:
                return True
        return False

    def play(self, board):
        if not board.game_over():
            board.put_chip_on_first_non_full_column(self._color)
