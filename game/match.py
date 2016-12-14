#!/usr/bin/env python
from gameboard import GameBoard
from game.player_with_strategy_one import PlayerWithStrategyOne
from game.player_with_strategy_two import PlayerWithStrategyTwo
from itertools import cycle

class GameIsOver(Exception): # Where should this exception be placed?
    def __init___(self, winner):
        self.winner = winner

class Match(object):
    def __init__(self, player_one = PlayerWithStrategyOne('red'),
                 player_two = PlayerWithStrategyTwo('blue'), board = GameBoard()):
        self._board = board
        self._active_player = None
        self._players = [player_one, player_two]
        self._player_iterator = cycle(self._players)
        self._switch_to_next_player()

    def play_next_turn(self):
        if self._board.game_over():
            raise GameIsOver(self.who_won)
        else:
            self._active_player.play(self._board)
        if not self._board.game_over():
            self._switch_to_next_player()

    def play_full_match(self):
        while not self._board.game_over():
            self.play_next_turn()
        return self.who_won()

    def is_over(self):
        return self._board.game_over()

    def who_won(self):
        for player in self._players:
            if player.is_winner(self._board):
                return player
        return None

    def _switch_to_next_player(self):
        self._active_player = self._player_iterator.next()
