#!/usr/bin/env python
from game.strategy_one import StrategyOne

class Player(object):

    def __init__(self, color):
        self._color = color.lower()
        self._strategy = StrategyOne()

    def set_strategy(self, strategy):
        self._strategy = strategy
        self._strategy.set_color(self._color)

    def color(self):
        return self._color

    def is_winner(self, board):
        return board.is_game_over() and board.winner_color() == self._color

    def play(self, board):
        column_to_play = self._strategy.return_column(board)
        board.put_chip(column_to_play, self._color)

    @classmethod
    def with_strategy(self, color, strategy):
        player = Player(color)
        player.set_strategy(strategy)
        return player
