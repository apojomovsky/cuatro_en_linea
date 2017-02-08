#!/usr/bin/env python
import unittest
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from game.first_non_full_column_strategy import FirstNonFullColumnStrategy

class TestFirstNonFullColumnStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = FirstNonFullColumnStrategy()
        self.color = 'blue'

    def test_strategy_choses_leftmost_column_on_empty_board(self):
        """
        This strategy returns the first column (leftmost)
        when the board is emtpy
        """
        board = GameBoard()
        self.assertEqual(self.strategy.return_column(board, self.color), 1)

    def test_strategy_on_near_empty_board(self):
        """
        The strategy looks from left to right for the first non-full column.
        The test expects the first column because it's not full.
        """
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 1)

    def test_strategy_on_near_full_column(self):
        """
        Even if the column is almost full, this strategy will choose it
        if it's the leftmost non full
        """
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 1)

    def test_strategy_choses_leftmost_non_full_column(self):
        """
        This strategy will choose column two, because it's the leftmost column
        that is not full
        """
        board = GameBoard.from_matrix([
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 2)

    def test_strategy_choses_the_only_non_full_column(self):
        """The strategy choses correctly the only column that is not full on the
           whole board
        """
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  None,  'blue', 'blue', 'blue'],
                    ['red',   'red', 'blue',  None,  'blue',  'red',  'red'],
                    ['red',  'blue',  'red',  None,  'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(self.strategy.return_column(board, self.color), 4)

    def test_strategy_raises_exception_on_full_board(self):
        """If it turns that the board is full, but the return_column message from
           the strategy is called, a BoardIsFull exception will be raised.
        """
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['red',   'red', 'blue',  'red', 'blue',  'red',  'red'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        with self.assertRaises(BoardIsFull):
            self.strategy.return_column(board, self.color)
