#!/usr/bin/env python
from .gameboard import GameBoard
from .player import Player
from itertools import cycle
import time

class Match(object):
    def __init__(self, player_one = Player('red'), player_two = Player('blue'), board = GameBoard(), active_player = None):
        self._board = board
        self._players = [player_one, player_two]
        self._player_iterator = cycle(self._players)
        if not active_player:
            self._active_player = self._player_iterator.next()

    def play_next_turn(self):
        self._active_player.play(self._board)
        if not self._board.game_over():
            self._active_player = self._player_iterator.next()

    def play_match(self):
        while not self._board.winner_exists():
            self.play_next_turn()
        return self.who_won()
        #return self._active_player


    def who_won(self):
        if self._board.winner_exists():
            for player in self._players:
                if player.color == self._board.winner_color():
                    return player
        return None
