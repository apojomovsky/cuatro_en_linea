#!/usr/bin/env python
from game.strategy_one import StrategyOne

class Player(object):

    def __init__(self, color, strategy=None):
        if strategy:
            self._strategy = strategy
        else:
            self._strategy = StrategyOne()
        self._color = color.lower()

    def color(self):
        return self._color

    def is_winner(self, board):
        return board.is_game_over() and board.winner_color() == self._color

    def play(self, board):
        board.put_chip(self._strategy.return_column(board), self._color)
