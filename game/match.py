#!/usr/bin/env python
from .gameboard import GameBoard
from .player import Player
from itertools import cycle
import time

class GameIsOver(Exception): # Where should this exception be placed?
    def __init___(self, winner):
        self.winner = winner

class Match(object):
    def __init__(self, player_one = Player('red'), player_two = Player('blue'), board = GameBoard()):
        self._board = board
        self._players = [player_one, player_two]
        self._player_iterator = cycle(self._players)
        self.active_player = self._player_iterator.next()


    def play_next_turn(self):
        if not self.is_over():
            self.active_player.play(self._board)
        else:
            raise GameIsOver(self.who_won)
        if not self.is_over():
            self.active_player = self._player_iterator.next()

    def play_full_match(self):
        while not self.is_over():
            self.play_next_turn()
        return self.who_won()

    def is_over(self):
        return self._board.game_over()

    def who_won(self):
        for player in self._players:
            if player.is_winner(self._board):
                return player
        return None
