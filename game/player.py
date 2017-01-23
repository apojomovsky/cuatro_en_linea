#!/usr/bin/env python
from game.strategy_one import StrategyOne

class Player(object):

    def __init__(self, color, strategy):
        self._color = color.lower()
        self._strategy = strategy

    def is_winner(self, board):
        return board.is_game_over() and board.winner_color() == self._color

    def play(self, board):
        column_to_play = self._strategy.return_column(board, self._color)
        board.put_chip(column_to_play, self._color)
