#!/usr/bin/env python
from game.gameboard import GameBoard

class Player(object):
    def __init__(self, color, gameboard):
        self._gameboard = gameboard
        self._color = color

    def color(self):
        return self._color

    def play(self):
        for index in range(1, GameBoard.COLUMNSCOUNT + 1):
            if not self._gameboard.column_is_full(index):
                self._gameboard.put_chip(index, self._color)
                self._gameboard.show()
                return True
