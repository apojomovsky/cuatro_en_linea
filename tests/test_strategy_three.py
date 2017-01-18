#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.strategy_three import StrategyThree

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_three = StrategyThree()
        self.strategy_three.set_color('blue')

    def test_strategy_three_choses_column_closest_to_win_for_blue(self):
        board = GameBoard.from_matrix([
                    [None,  None,   None, None, None, None, None],
                    [None,  None,   None, None, None, None, None],
                    [None,  None,   None, None, None, None, None],
                    ['red', None, 'blue', None, None, None, None],
                    ['red', None, 'blue', None, None, None, None],
                    ['red', None, 'blue', None, None, None, None]])
        self.assertEqual(self.strategy_three.return_column(board), 3)

    def test_strategy_three_choses_sixth_column_because_unable_to_win_on_leftmost(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None,    None],
                    ['blue', None, None, None, None, None,    None],
                    ['blue', None, None, None, None, None,    None],
                    ['red',  None, None, None, None, None,    None],
                    ['red',  None, None, None, None, 'blue',  None],
                    ['red',  None, None, None, None, 'blue', 'blue']])
        self.assertEqual(6, self.strategy_three.return_column(board))

    def test_strategy_three_choses_leftmost_when_more_than_one_evaluates_equal(self):
        board = GameBoard.from_matrix([
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None, 'blue', 'blue',  None, None,  None],
                    ['red', 'red', 'blue', 'blue', 'red', 'red', None]])
        self.assertEqual(self.strategy_three.return_column(board), 3)

    def test_strategy_three_choses_leftmost_column_from_empty_board(self):
        board = GameBoard()
        self.assertEqual(1, self.strategy_three.return_column(board))

    def test_strategy_three_choses_first_non_full_column_when_unable_to_win(self):
        board = GameBoard.from_matrix([
                    [None,     None,   None,   None,   None,   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red',  'red'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(1, self.strategy_three.return_column(board))
