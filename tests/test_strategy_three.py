#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.strategy_three import StrategyThree

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_three = StrategyThree()
        self.strategy_three.set_color('blue')

    def test_strategy_three_on_sixth_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,   None,   None,   None],
                    ['blue',   None,   None,   None,   None,   None,   None],
                    ['blue',   None,  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red']])
        self.assertEqual(6, self.strategy_three.return_column(board))

    def test_strategy_three_red_on_seventh_column_because_cannot_win_on_first(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None,   None],
                    ['red',  None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']])
        self.assertEqual(7, self.strategy_three.return_column(board))


    def test_strategy_three_blue_on_first_column_from_empty_board(self):
        board = GameBoard.from_matrix([
                    [None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None]])
        self.assertEqual(1, self.strategy_three.return_column(board))

    def test_strategy_three_on_impossible_to_win_board_(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',   None,   None],
                    ['red',  'blue',  'red',  'red', 'blue',   None, 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red',  'red'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(6, self.strategy_three.return_column(board))
