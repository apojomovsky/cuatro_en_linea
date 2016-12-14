#!/usr/bin/env python
import unittest
from game.match import Match
from game.player_with_strategy_two import PlayerWithStrategyTwo
from game.player import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = PlayerWithStrategyTwo('blue')
        self.player_red = PlayerWithStrategyTwo('red')

    def test_player_wins_with_strategy_two(self):
        self.board_player_red_wins = GameBoard.from_matrix([
                    ['blue', 'blue', None,  None,   None,   None, None],
                    ['red',   'red',  None, None, 'blue', 'blue', None],
                    ['blue',  'red', None,  None,  'red', 'blue', None],
                    ['blue',  'red', 'blue',  None, 'blue',  'red', None],
                    ['blue', 'blue', 'blue',  None,  'red', 'blue', None],
                    ['red',   'red',  'red', 'blue',  'red', 'blue', None]])
        self.match = Match(self.player_blue, self.player_red, self.board_player_red_wins)
        self.assertFalse(self.player_red.is_winner(self.board_player_red_wins))
        for i in range(5):
            self.match.play_next_turn()
            self.assertFalse(self.player_red.is_winner(self.board_player_red_wins))
        self.match.play_next_turn()
        self.assertTrue(self.player_red.is_winner(self.board_player_red_wins))
