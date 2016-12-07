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
    def play(self):
        """This method must be overridden"""
        pass

class PlayerWithStrategyOne(Player):
    def play(self, board):
        board.put_chip(board.retrieve_first_non_full_column(), self._color)

class PlayerWithStrategyTwo(Player):
    def play(self, board):
        board.put_chip(board.retrieve_emptiest_column(), self._color)
