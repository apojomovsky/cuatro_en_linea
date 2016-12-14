#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from game.gameboard import GameBoard

class Player(object):
    __metaclass__ = ABCMeta

    def __init__(self, color):
        self._color = color.lower()

    def color(self):
        return self._color

    def is_winner(self, board):
        if board.game_over() and board.winner_color() == self._color:
            return True
        return False

    @abstractmethod
    def play(self, board):
        """This method must be overridden"""
        pass
