#!/usr/bin/env python
from game.player import Player

class PlayerWithStrategyTwo(Player):
    def play(self, board):
        board.put_chip(board.retrieve_emptiest_column(), self._color)
