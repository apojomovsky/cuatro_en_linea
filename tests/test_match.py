#!/usr/bin/env python
import unittest
from game.match import Match
from game.match import GameIsOver
from game.player import Player
from game.first_non_full_column_strategy import FirstNonFullColumnStrategy
from game.emptiest_column_strategy import EmptiestColumnStrategy
from game.gameboard import GameBoard

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.player_white = Player('W', FirstNonFullColumnStrategy())
        self.player_black = Player('B', EmptiestColumnStrategy())
        self.match = Match(self.player_white, self.player_black, GameBoard())

    def test_play_next_turn_on_running_match(self):
        match_white_win_from_row = Match(self.player_white, self.player_black,
                                            GameBoard.from_matrix([
                    [None,   'W',  'W',  'W',   None,   None, None],
                    ['W', 'B',  'W', 'B',   None,   None, None],
                    ['B', 'W', 'B',  'W',   None,   None, None],
                    ['B', 'W',  'W', 'B',   None,   None, None],
                    ['W', 'B',  'W', 'B',   None,   None, None],
                    ['B', 'W', 'B',  'W',  'W',  'W', None]]))
        self.assertFalse(match_white_win_from_row.is_over())
        match_white_win_from_row.play_next_turn()
        self.assertTrue(match_white_win_from_row.is_over())

    def test_play_next_turn_after_match_has_finished(self):
        match_white_won_from_row = Match(self.player_white, self.player_black,
                                       GameBoard.from_matrix([
                    ['W',  'W',  'W',  'W',   None,   None, None],
                    ['W', 'B',  'W', 'B',   None,   None, None],
                    ['B', 'W', 'B',  'W',   None,   None, None],
                    ['B', 'W',  'W', 'B',   None,   None, None],
                    ['W', 'B',  'W', 'B',   None,   None, None],
                    ['B', 'W', 'B',  'W',  'W',  'W', None]]))
        self.assertTrue(match_white_won_from_row.is_over())
        with self.assertRaises(GameIsOver):
            match_white_won_from_row.play_next_turn()

    def test_play_full_match_and_white_wins(self):
        self.assertFalse(self.match.is_over())
        self.match.play_full_match()
        self.assertTrue(self.match.is_over())
        self.assertEqual(self.match.who_won(), self.player_white)

    def test_play_match_and_black_wins(self):
        match_black_win_with_row = Match(self.player_black, self.player_white,
                                        GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['B', None, None, None, None, None, 'B'],
                    ['B', None, None, None, None, None, 'B'],
                    ['B', None, None, None, None, None, 'B'],
                    ['W',  None, None, None, None, None,  'W'],
                    ['W',  None, None, None, None, None,  'W']]))
        self.assertFalse(match_black_win_with_row.is_over())
        match_black_win_with_row.play_full_match()
        self.assertTrue(match_black_win_with_row.is_over())
        self.assertEqual(match_black_win_with_row.who_won(), self.player_black)

    def test_who_won_when_black_won(self):
        match_with_almost_full_board = Match(self.player_black, self.player_white,
                                             GameBoard.from_matrix([
                    ['B', 'B',  'W',   None, 'B', 'B', 'B'],
                    ['W',   'W', 'B',  'W', 'B',  'W', 'B'],
                    ['B', 'B',  'W', 'B',  'W', 'B',  'W'],
                    ['W',  'B',  'W',  'W',  'W', 'B', 'B'],
                    ['B',  'W', 'B', 'B', 'B',  'W',  'W'],
                    ['W',  'B', 'B',  'W', 'B',  'W', 'B']]))
        self.assertFalse(match_with_almost_full_board.is_over())
        match_with_almost_full_board.play_next_turn()
        self.assertTrue(match_with_almost_full_board.is_over())
        self.assertEqual(match_with_almost_full_board.who_won(), self.player_black)
