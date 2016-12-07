#!/usr/bin/env python
import unittest
from game.match import Match
from game.player import PlayerWithStrategyOne
from game.player import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.player_blue = PlayerWithStrategyOne('blue')
        self.player_red = PlayerWithStrategyOne('red')

    def test_player_wins_with_strategy_one(self):
        self.board_player_blue_wins = GameBoard.from_matrix([
                    ['blue', 'blue', 'blue',  'red',   None,   None, None],
                    ['red',   'red',  'red', 'blue', 'blue',   None, None], # <- blue row wins
                    ['blue',  'red', 'blue',  'red', 'blue',   None, None],
                    ['blue',  'red', 'blue',  'red',  'red',  'red', None],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', None],
                    ['red',   'red',  'red', 'blue',  'red', 'blue', None]])
        self.match = Match(self.player_blue, self.player_red, self.board_player_blue_wins)
        self.assertFalse(self.player_blue.is_winner(self.board_player_blue_wins))
        self.match.play_full_match()
        self.assertTrue(self.player_blue.is_winner(self.board_player_blue_wins))
