#!/usr/bin/env python
from gameboard import GameBoard
from game.player import Player
from itertools import cycle

class GameIsOver(Exception):
    def __init___(self, winner):
        self.winner = winner

class Match(object):
    def __init__(self, player_one, player_two, board):
        self._board = board
        self._active_player = None
        self._player_one = player_one
        self._player_two = player_two
        self._player_iterator = cycle(self._players())
        self._switch_to_next_player()

    def _players(self):
        return [self._player_one, self._player_two]

    def play_next_turn(self):
        if self._board.is_game_over():
            raise GameIsOver(self.who_won)
        else:
            self._active_player.play(self._board)
        if not self._board.is_game_over():
            self._switch_to_next_player()

    def play_full_match(self):
        while not self._board.is_game_over():
            self.play_next_turn()
        return self.who_won()

    def is_over(self):
        return self._board.is_game_over()

    def who_won(self):
        for player in self._players():
            if player.is_winner(self._board):
                return player
        return None

    def _switch_to_next_player(self):
        self._active_player = self._player_iterator.next()
