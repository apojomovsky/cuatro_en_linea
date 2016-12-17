#!/usr/bin/env python
import unittest
from game.match import Match
from game.player_with_strategy_one import PlayerWithStrategyOne
from game.player import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = PlayerWithStrategyOne('blue')
        self.player_red = PlayerWithStrategyOne('red')

    def test_player_with_strategy_one_blue_wins_on_right_upper_corner(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',  'blue',   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(board.read_entry(6, 7), None)
        self.assertFalse(self.player_blue.is_winner(board))
        self.player_blue.play(board)
        self.assertEqual(board.read_entry(6, 7), 'blue')
        self.assertTrue(self.player_blue.is_winner(board))

    def test_player_with_strategy_one_blue_wins_on_left_corner(self):
        board = GameBoard.from_matrix([
                    [None,    None,    None,  None, 'blue',  'blue',   None],
                    ['blue',   None,   None,  'red',  'red',  'red', 'blue'],
                    ['blue', 'blue',   None,  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(board.read_entry(6, 1), None)
        self.assertFalse(self.player_blue.is_winner(board))
        self.player_blue.play(board)
        self.assertEqual(board.read_entry(6, 1), 'blue')
        self.assertTrue(self.player_blue.is_winner(board))

    def test_player_with_strategy_one_red_not_winning_on_column(self):
        board = GameBoard.from_matrix([
                    [None,     None,   None,   None,  None, None, None],
                    [None,     None,   None,   None,  None, None, None],
                    ['red',  'blue',   None, 'blue',  None, None, None],
                    ['blue', 'blue',   None, 'blue',  None, None, None],
                    ['red',  'blue',  'red', 'blue',  None, None, None],
                    ['blue',  'red', 'blue',  'red', 'red', None, None]])
        self.assertEqual(board.read_entry(5, 1), None)
        self.assertEqual(board.read_entry(5, 2), None)
        self.assertEqual(board.read_entry(5, 4), None)
        self.assertFalse(self.player_blue.is_winner(board))
        self.player_blue.play(board)
        self.assertEqual(board.read_entry(5, 1), 'blue')
        self.assertEqual(board.read_entry(5, 2), None)
        self.assertEqual(board.read_entry(5, 4), None)
        self.assertFalse(self.player_blue.is_winner(board))

    def test_player_with_strategy_one_red_not_winning_on_row(self):
        board = GameBoard.from_matrix([
                    [None,    None,    None,   None,  None,  None, None],
                    [None,    None,    None,   None,  None,  None, None],
                    [None,    None,    None,   None,  None,  None, None],
                    ['red',   'red',  'red',   None,  None,  None, None],
                    ['blue',  'red', 'blue', 'blue',  None,  None, None],
                    ['blue', 'blue', 'blue',  'red', 'red', 'red', None]])
        self.assertEqual(board.read_entry(4, 1), None)
        self.assertEqual(board.read_entry(3, 4), None)
        self.assertEqual(board.read_entry(1, 7), None)
        self.assertFalse(self.player_red.is_winner(board))
        self.player_red.play(board)
        self.assertEqual(board.read_entry(4, 1), 'red')
        self.assertEqual(board.read_entry(3, 4), None)
        self.assertEqual(board.read_entry(1, 7), None)
        self.assertFalse(self.player_red.is_winner(board))
