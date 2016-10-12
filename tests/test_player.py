#!/usr/bin/env python
import unittest
from game.match import Match
from game.player import Player
from game.player import GameBoard


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.player_one = Player('blue')
        self.player_two = Player('red')
        self.board_player_one_win = GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']])

    def test_play_for_player_one_winning(self):
        self.assertFalse(self.player_one.is_winner(self.board_player_one_win))
        self.player_one.play(self.board_player_one_win)
        self.assertTrue(self.player_one.is_winner(self.board_player_one_win))
