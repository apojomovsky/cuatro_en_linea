#!/usr/bin/env python
import unittest
from game.match import Match
from game.player import PlayerWithStrategyTwo
from game.player import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.player_blue = PlayerWithStrategyTwo('blue')
        self.player_red = PlayerWithStrategyTwo('red')

    def test_player_wins_with_strategy_two(self):
        self.board_player_blue_wins = GameBoard.from_matrix([
                    ['blue', 'blue', 'blue',  'red',   None,   None, None],
                    ['red',   'red',  'red', 'blue', 'blue', 'blue', None], # <- blue row
                    ['blue',  'red', 'blue',  'red',  'red', 'blue', None],
                    ['blue',  'red', 'blue',  'red', 'blue',  'red', None],
                    ['blue', 'blue', 'blue',  'red',  'red', 'blue', None],
                    ['red',   'red',  'red', 'blue',  'red', 'blue', None]])
        self.match = Match(self.player_blue, self.player_red, self.board_player_blue_wins)
        self.assertFalse(self.player_blue.is_winner(self.board_player_blue_wins))
        self.match.play_full_match()
        self.assertTrue(self.player_blue.is_winner(self.board_player_blue_wins))
