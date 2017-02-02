#!/usr/bin/env python
from gameboard import GameBoard

class GameBoardView(object):
    def __init__(self, board):
        self._board = board

    def show(self):
        """Print the board of a given gameboard in a nice format"""
        print(chr(27) + "[2J")
        rows_iter = self._board.get_rows()
        for row in rows_iter:
            for entry in row:
                print '{:4}'.format(entry),
            print
        print
