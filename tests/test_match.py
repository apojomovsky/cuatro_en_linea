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
        self.white_player = Player('W', FirstNonFullColumnStrategy())
        self.black_player = Player('B', EmptiestColumnStrategy())
        self.match = Match(self.white_player, self.black_player, GameBoard())

    def test_play_next_turn_on_running_match(self):
        match_black_win_from_row = Match(self.white_player, self.black_player,
                                            GameBoard.from_matrix([
                    [None, 'B', 'B', 'B', None, None, None],
                    ['B',  'W', 'B', 'W', None, None, None],
                    ['W',  'B', 'W', 'B', None, None, None],
                    ['W',  'B', 'B', 'W', None, None, None],
                    ['B',  'W', 'B', 'W', None, None, None],
                    ['W',  'B', 'W', 'B',  'B',  'B', None]]))
        self.assertFalse(match_black_win_from_row.is_over())
        match_black_win_from_row.play_next_turn()
        self.assertTrue(match_black_win_from_row.is_over())

    def test_play_next_turn_after_match_has_finished(self):
        match_white_won_from_row = Match(self.white_player, self.black_player,
                                       GameBoard.from_matrix([
                    ['B', 'B', 'B', 'B', None, None, None],
                    ['B', 'W', 'B', 'W', None, None, None],
                    ['W', 'B', 'W', 'B', None, None, None],
                    ['W', 'B', 'B', 'W', None, None, None],
                    ['B', 'W', 'B', 'W', None, None, None],
                    ['W', 'B', 'W', 'B',  'B',  'B', None]]))
        self.assertTrue(match_white_won_from_row.is_over())
        with self.assertRaises(GameIsOver):
            match_white_won_from_row.play_next_turn()

    def test_play_full_match_and_white_wins(self):
        self.assertFalse(self.match.is_over())
        self.match.play_full_match()
        self.assertTrue(self.match.is_over())
        self.assertEqual(self.match.who_won(), self.white_player)

    def test_play_match_and_black_wins(self):
        match_white_win_with_row = Match(self.black_player, self.white_player,
                                         GameBoard.from_matrix([
                    [None, None, None, None, None, None, None],
                    ['W',  None, None, None, None, None,  'W'],
                    ['W',  None, None, None, None, None,  'W'],
                    ['W',  None, None, None, None, None,  'W'],
                    ['B',  None, None, None, None, None,  'B'],
                    ['B',  None, None, None, None, None,  'B']]))
        self.assertFalse(match_white_win_with_row.is_over())
        match_white_win_with_row.play_full_match()
        self.assertTrue(match_white_win_with_row.is_over())
        self.assertEqual(match_white_win_with_row.who_won(), self.white_player)

    def test_who_won_when_black_won(self):
        match_with_almost_full_board = Match(self.white_player, self.black_player,
                         GameBoard.from_matrix([
                    ['W', 'W', 'B', None, 'W', 'W', 'W'],
                    ['B', 'B', 'W',  'B', 'W', 'B', 'W'],
                    ['W', 'W', 'B',  'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B',  'B', 'B', 'W', 'W'],
                    ['W', 'B', 'W',  'W', 'W', 'B', 'B'],
                    ['B', 'W', 'W',  'B', 'W', 'B', 'W']]))
        self.assertFalse(match_with_almost_full_board.is_over())
        match_with_almost_full_board.play_next_turn()
        self.assertTrue(match_with_almost_full_board.is_over())
        self.assertEqual(match_with_almost_full_board.who_won(), self.white_player)
