#!/usr/bin/env python
import unittest
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from game.emptiest_column import EmptiestColumn

class TestStrategyEmptiestColumn(unittest.TestCase):
    def setUp(self):
        self.strategy = EmptiestColumn()
        self.color = 'blue'

    def test_strategy_choses_leftmost_column_on_empty_board(self):
        """
        Strategy_two will return the first column (leftmost)
        if the board is emtpy
        """
        board = GameBoard()
        self.assertEqual(self.strategy.return_column(board, self.color), 1)

    def test_strategy_choses_emptiest_rightmost_column(self):
        """
        If only the rightmost entry from the first row is empty,
        strategy_two will choose the rightmost column, because it's the emptiest
        """
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    ['red', 'blue', 'blue', 'blue', 'red', 'blue', None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 7)

    def test_strategy_choses_emptiest_leftmost_column(self):
        """
        If only the leftmost entry from the first row is empty,
        strategy_two will choose the leftmost column, because it's the emptiest
        """
        board = GameBoard.from_matrix([
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None, 'blue', 'blue', 'blue', 'red', 'blue', 'red']])
        self.assertEqual(self.strategy.return_column(board, self.color), 1)

    def test_strategy_choses_leftmost_empty_when_more_than_one_equally_empty(self):
        """
        If more than one column has the same number of free entries, strategy_two
        will priorize the leftmost. In this case will choose column 3 instead of 4
        """
        board = GameBoard.from_matrix([
                    [None,     None, None,  None,  None,   None,   None],
                    [None,     None, None,  None,  None,   None,   None],
                    [None,     None, None,  None,  None,   None,   None],
                    [None,     None, None,  None,  None,   None,   None],
                    ['red',  'blue', None,  None, 'blue', 'red', 'blue'],
                    ['blue',  'red', 'red', 'red', 'red', 'blue', 'red']])
        self.assertEqual(self.strategy.return_column(board, self.color), 3)

    def test_strategy_choses_emptiests_column_from_mid_loaded_board(self):
        """
        On a mid-loaded board, with almost all columns equally loaded, strategy_two
        will choose the one that is emptier than the rest.
        """
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,   None,   None,   None],
                    [None,    None,   None,   None,   None,   None,   None],
                    [None,    None,   None,   None,   None,   None,   None],
                    ['red', 'blue',  'red',   None,  'red', 'blue', 'blue'],
                    ['red', 'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'red', 'blue', 'blue', 'blue',  'red',  'red']])
        self.assertEqual(self.strategy.return_column(board, self.color), 4)

    def test_strategy_raises_exception_when_board_is_full(self):
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
