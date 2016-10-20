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

    def play_on_first_non_full_column(self, board, right_to_left=False):
        if right_to_left:
            board.put_chip(board.retrieve_first_non_full_column(right_to_left), self._color)
        else:
            board.put_chip(board.retrieve_first_non_full_column(), self._color)

    def play_on_emptiest_column(self, board, right_to_left=False):
        if right_to_left:
            board.put_chip(board.retrieve_emptiest_column(right_to_left), self._color)
        else:
            board.put_chip(board.retrieve_emptiest_column(), self._color)
