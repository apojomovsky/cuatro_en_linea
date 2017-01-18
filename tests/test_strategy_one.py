#!/usr/bin/env python
import unittest
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from game.strategy_one import StrategyOne

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_one = StrategyOne()
        self.color = 'blue'

    def test_strategy_two_choses_leftmost_column_on_empty_board(self):
        board = GameBoard()
        self.assertEqual(self.strategy_one.return_column(board), 1)

    def test_strategy_one_on_near_empty_board(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(self.strategy_one.return_column(board), 1)

    def test_strategy_one_on_near_full_column(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(self.strategy_one.return_column(board), 1)

    def test_strategy_one_choses_leftmost_non_full_column(self):
        board = GameBoard.from_matrix([
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(self.strategy_one.return_column(board), 2)

    def test_strategy_one_raises_exception_on_full_board(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['red',   'red', 'blue',  'red', 'blue',  'red',  'red'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        with self.assertRaises(BoardIsFull):
            self.strategy_one.return_column(board)
