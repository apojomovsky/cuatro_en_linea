#!/usr/bin/env python
import unittest
from game.match import Match
from game.match import GameIsOver
from game.player import Player
from game.player import PlayerWithStrategyOne
from game.player import PlayerWithStrategyTwo
from game.gameboard import GameBoard

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.player_red = PlayerWithStrategyOne('red')
        self.player_blue = PlayerWithStrategyTwo('blue')
        self.match = Match(self.player_red, self.player_blue)

    def test_play_next_turn_on_running_match(self):
        self.match_red_win_from_row = Match(self.player_red, self.player_blue, GameBoard.from_matrix([
                    [None,   'red',  'red',  'red',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',   None,   None, None],
                    ['blue', 'red',  'red', 'blue',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',  'red',  'red', None]]))
        self.assertFalse(self.match_red_win_from_row.is_over())
        self.match_red_win_from_row.play_next_turn()
        self.assertTrue(self.match_red_win_from_row.is_over())

    def test_play_next_turn_after_match_has_finished(self):
        self.match_red_won_from_row = Match(self.player_red, self.player_blue, GameBoard.from_matrix([
                    ['red',  'red',  'red',  'red',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',   None,   None, None],
                    ['blue', 'red',  'red', 'blue',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',  'red',  'red', None]]))
        self.assertTrue(self.match_red_won_from_row.is_over())
        with self.assertRaises(GameIsOver):
            self.match_red_won_from_row.play_next_turn()

    def test_play_full_match_when_red_wins(self):
        self.assertFalse(self.match.is_over())
        self.match.play_full_match()
        self.assertTrue(self.match.is_over())
        self.assertEqual(self.match.who_won(), self.player_red)

    def test_play_match_when_blue_wins(self):
        self.match_blue_win_with_row = Match(self.player_blue, self.player_red, GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']]))
        self.assertFalse(self.match_blue_win_with_row.is_over())
        self.match_blue_win_with_row.play_full_match()
        self.assertTrue(self.match_blue_win_with_row.is_over())
        self.assertEqual(self.match_blue_win_with_row.who_won(), self.player_blue)

    def test_who_won_when_blue_wins(self):
        self.match_with_almost_full_board = Match(self.player_blue, self.player_red, GameBoard.from_matrix([
                    ['blue', 'blue',  'red',   None, 'blue', 'blue', 'blue'],
                    ['red',   'red', 'blue',  'red', 'blue',  'red', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']]))
        self.assertFalse(self.match_with_almost_full_board.is_over())
        self.match_with_almost_full_board.play_next_turn()
        self.assertTrue(self.match_with_almost_full_board.is_over())
        self.assertEqual(self.match_with_almost_full_board.who_won(), self.player_blue)
