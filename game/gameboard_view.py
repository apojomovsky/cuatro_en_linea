#!/usr/bin/env python
from gameboard import GameBoard

class GameBoardView(object):

    def show(self, board):
        """Print the board of a given gameboard in a nice format"""
        print(chr(27) + "[2J")
        for row in board.retrieve_matrix():
            for entry in row:
                print '{:4}'.format(entry),
            print
        print
