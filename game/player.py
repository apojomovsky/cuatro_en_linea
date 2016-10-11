#!/usr/bin/env python
from game.gameboard import GameBoard

class Player(object):
    def __init__(self, color):
        self._color = color

    def color(self):
        return self._color

    def play(self, board):
        if not board.game_over():
            board.put_chip_on_first_non_full_column(self._color)
