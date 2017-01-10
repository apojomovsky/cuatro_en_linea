#!/usr/bin/env python
import unittest
from game.match import Match
from game.match import GameIsOver
from game.player import Player
from game.strategy_one import StrategyOne
from game.strategy_two import StrategyTwo
from game.gameboard import GameBoard

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.player_red = Player.with_strategy('red', StrategyOne())
        self.player_blue = Player.with_strategy('blue', StrategyTwo())
        self.match = Match(self.player_red, self.player_blue)

    def test_play_next_turn_on_running_match(self):
        match_red_win_from_row = Match(self.player_red, self.player_blue,
                                            GameBoard.from_matrix([
                    [None,   'red',  'red',  'red',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',   None,   None, None],
                    ['blue', 'red',  'red', 'blue',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',  'red',  'red', None]]))
        self.assertFalse(match_red_win_from_row.is_over())
        match_red_win_from_row.play_next_turn()
        self.assertTrue(match_red_win_from_row.is_over())

    def test_play_next_turn_after_match_has_finished(self):
        match_red_won_from_row = Match(self.player_red, self.player_blue,
                                       GameBoard.from_matrix([
                    ['red',  'red',  'red',  'red',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',   None,   None, None],
                    ['blue', 'red',  'red', 'blue',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',  'red',  'red', None]]))
        self.assertTrue(match_red_won_from_row.is_over())
        with self.assertRaises(GameIsOver):
            match_red_won_from_row.play_next_turn()

    def test_play_full_match_and_red_wins(self):
        self.assertFalse(self.match.is_over())
        self.match.play_full_match()
        self.assertTrue(self.match.is_over())
        self.assertEqual(self.match.who_won(), self.player_red)

    def test_play_match_and_blue_wins(self):
        match_blue_win_with_row = Match(self.player_blue, self.player_red,
                                        GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']]))
        self.assertFalse(match_blue_win_with_row.is_over())
        match_blue_win_with_row.play_full_match()
        self.assertTrue(match_blue_win_with_row.is_over())
        self.assertEqual(match_blue_win_with_row.who_won(), self.player_blue)

    def test_who_won_when_blue_won(self):
        match_with_almost_full_board = Match(self.player_blue, self.player_red,
                                             GameBoard.from_matrix([
                    ['blue', 'blue',  'red',   None, 'blue', 'blue', 'blue'],
                    ['red',   'red', 'blue',  'red', 'blue',  'red', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']]))
        self.assertFalse(match_with_almost_full_board.is_over())
        match_with_almost_full_board.play_next_turn()
        self.assertTrue(match_with_almost_full_board.is_over())
        self.assertEqual(match_with_almost_full_board.who_won(), self.player_blue)
