#!/usr/bin/env python
from .gameboard import GameBoard
from .player import Player

class Match(object):
    def __init__(self):
        self.game = GameBoard()
        self.players = {'red': Player('red', self.game), 'blue': Player('blue', self.game)}
        self.start_time = time.time()
        self._active_player = self.players.get('red')

    def next_turn(self):
        if self._active_player == self.players.get('blue'):
            self._active_player = self.players.get('red')
        else:
            self._active_player = self.players.get('blue')

    def whos_turn(self):
        return self._active_player.color()

    def play_match(self):
        while not self.game.winner_exists():
            self.next_turn()
            self.players.get(self._active_player).play()
            self.game.show()
        return self.game.who_won()
