#!/usr/bin/env python
from game.gameboard import GameBoard

class GameBoardView(object):

    def show(self, board):
        """Print the board of a given gameboard in a nice format"""
        for row in board.retrieve_matrix():
            for entry in row:
                print '{:4}'.format(entry),
            print
        print
