#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from game.strategy_one import StrategyOne

class Player(object):
    __metaclass__ = ABCMeta

    def __init__(self, color, strategy = StrategyOne()):
        self._color = color.lower()
        self._strategy = strategy

    def color(self):
        return self._color

    def set_strategy(self, new_strategy):
        self._strategy = new_strategy

    def is_winner(self, board):
        return board.is_game_over() and board.winner_color() == self._color

    def play(self, board):
        board.put_chip(self._strategy.return_column(board), self._color)
