#!/usr/bin/env python
import unittest
from game.gameboard import GameBoard
from game.strategy_one import StrategyOne

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_one = StrategyOne('blue')

    def test_strategy_one_on_sixth_column(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',   None,   None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',   None],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(self.strategy_one.return_column(board), 6)

    def test_strategy_one_on_second_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None, None, None, None, None, None],
                    ['blue',   None, None, None, None, None, None],
                    ['red',    None, None, None, None, None, None],
                    ['blue',   None, None, None, None, None, None],
                    ['red',   'red', None, None, None, None, None],
                    ['blue', 'blue', None, None, None, None, None]])
        self.assertEqual(self.strategy_one.return_column(board), 2)

    def test_strategy_on_first(self):
        board = GameBoard.from_matrix([
                    [None,     None,   None,   None,  None, None, None],
                    ['blue',   None,   None,   None,  None, None, None],
                    ['red',  'blue',   None, 'blue',  None, None, None],
                    ['blue', 'blue',   None, 'blue',  None, None, None],
                    ['red',  'blue',  'red', 'blue',  None, None, None],
                    ['blue',  'red', 'blue',  'red', 'red', None, None]])
        self.assertEqual(self.strategy_one.return_column(board), 1)
