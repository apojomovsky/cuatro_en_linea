#!/usr/bin/env python
from game.player import Player

class PlayerWithStrategyOne(Player):
    def play(self, board):
        board.put_chip(board.retrieve_first_non_full_column(), self._color)
