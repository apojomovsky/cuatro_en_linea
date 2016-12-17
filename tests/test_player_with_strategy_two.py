#!/usr/bin/env python
import unittest
from game.player_with_strategy_two import PlayerWithStrategyTwo
from game.gameboard import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = PlayerWithStrategyTwo('blue')
        self.player_red = PlayerWithStrategyTwo('red')

    def test_player_with_strategy_two_blue_wins_on_right_almost_upper_corner(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,   None,   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red',   None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(board.read_entry(5, 7), None)
        self.player_blue.play(board)
        self.assertEqual(board.read_entry(5, 7), 'blue')


    def test_player_with_strategy_two_blue_wins_on_left_lower_corner(self):
        board = GameBoard.from_matrix([
                    [None,   None,   None,   None,  None, None,   None],
                    [None,   None,   None,   None,  None, None,   None],
                    [None,   None,   None,   None,  None, None, 'red'],
                    [None,  'red',   None,   None,  None, None, 'blue'],
                    [None, 'blue',   None, 'blue',  None, None, 'blue'],
                    [None, 'blue', 'blue', 'blue',  None, None,  'red']])
        self.assertEqual(board.read_entry(1, 1), None)
        self.player_blue.play(board)
        self.assertEqual(board.read_entry(1, 1), 'blue')


    def test_player_with_strategy_two_red_not_winning_on_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,    None,   None,   None],
                    ['blue',   None,   None,   None,    None,   None,   None],
                    ['blue',   None,  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red',  'red',   'red', 'blue', 'blue'],
                    ['red',  'blue',  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'blue', 'blue',  'red',  'red']])
        self.assertEqual(board.read_entry(4, 2), None)
        self.assertEqual(board.read_entry(5, 3), None)
        self.assertEqual(board.read_entry(5, 4), None)
        self.player_red.play(board)
        self.assertEqual(board.read_entry(4, 2), 'red')
        self.assertEqual(board.read_entry(5, 3), None)
        self.assertEqual(board.read_entry(5, 4), None)

    def test_player_with_strategy_two_red_not_winning_on_row(self):
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,   None,   None,   None],
                    [None,    None,   None,  'red',  'red',  'red',   None],
                    [None,    None,  'red',  'red',  'red', 'blue', 'blue'],
                    [None,  'blue',  'red', 'blue',  'blue', 'red', 'blue'],
                    ['red', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue', 'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(board.read_entry(3, 1), None)
        self.assertEqual(board.read_entry(4, 2), None)
        self.assertEqual(board.read_entry(5, 3), None)
        self.assertEqual(board.read_entry(5, 7), None)
        self.player_red.play(board)
        self.assertEqual(board.read_entry(3, 1), 'red')
        self.assertEqual(board.read_entry(4, 2), None)
        self.assertEqual(board.read_entry(5, 3), None)
        self.assertEqual(board.read_entry(5, 7), None)
