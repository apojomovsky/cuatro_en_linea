#!/usr/bin/env python
import unittest
from game.gameboard import GameBoard
from game.strategy_two import StrategyTwo

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_two = StrategyTwo('blue')

    def test_strategy_two_on_seventh_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,   None,   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red',   None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(self.strategy_two.return_column(board), 7)

    def test_strategy_two_on_sixth_column(self):
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,  'blue',   None, 'blue',  None, None, 'blue'],
                    ['red', 'blue', 'blue', 'blue', 'red', None,  'red']])
        self.assertEqual(self.strategy_two.return_column(board), 6)

    def test_strategy_two_on_second_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,    None,   None,   None],
                    ['blue',   None,   None,   None,    None,   None,   None],
                    ['blue',   None,  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red',  'red',   'red', 'blue', 'blue'],
                    ['red',  'blue',  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'blue', 'blue',  'red',  'red']])
        self.assertEqual(self.strategy_two.return_column(board), 2)
