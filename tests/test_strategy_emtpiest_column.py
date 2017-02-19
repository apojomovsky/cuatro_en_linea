#!/usr/bin/env python
import unittest
from board_builder import BoardBuilder
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from game.emptiest_column_strategy import EmptiestColumnStrategy

class TestEmptiestColumnStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = EmptiestColumnStrategy()
        self.color = 'W'
        self.builder = BoardBuilder('W', 'B')

    def test_strategy_choses_leftmost_column_on_empty_board(self):
        """
        Strategy_two will return the first column (leftmost)
        if the board is empty
        """
        board = GameBoard()
        self.assertEqual(self.strategy.return_column(board, self.color), 1)

    def test_strategy_choses_emptiest_rightmost_column(self):
        """
        If only the rightmost entry from the first row is empty,
        strategy_two will choose the rightmost column, because it's the emptiest
        """
        test_board = self.builder.build_from_moves([1,2,5,3,4,6])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W B B W W B .
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 7)

    def test_strategy_choses_emptiest_leftmost_column(self):
        """
        If only the leftmost entry from the first row is empty,
        strategy_two will choose the leftmost column, because it's the emptiest
        """
        test_board = self.builder.build_from_moves([2,4,3,5,6,7])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . W W B B W B
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 1)

    def test_strategy_choses_leftmost_empty_when_more_than_one_equally_empty(self):
        """
        If more than one column has the same number of free entries, strategy_two
        will priorize the leftmost. In this case will choose column 3 instead of 4
        """
        test_board = self.builder.build_from_moves([1,2,6,7,7,3,2,5,5,4,1,6])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W W . . W B W
        W B B B B W B
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 3)

    def test_strategy_choses_emptiests_column_from_mid_loaded_board(self):
        """
        On a mid-loaded board, with almost all columns equally loaded, strategy_two
        will choose the one that is emptier than the rest.
        """
        test_board = self.builder.build_from_moves(
        [4,7,1,1,2,3,5,5,3,6,4,3,1,5,2,2,6,7,6,7])

        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W B B . B W B
        B W W W B W B
        W W B W W B B
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 4)

    def test_strategy_raises_exception_when_board_is_full(self):
        """If it turns that the board is full, but the return_column message from
           the strategy is called, a BoardIsFull exception will be raised.
        """
        board = self.builder.build_from_moves(
            [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
             3,4,3,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7])
        """
        W W W B W W W
        B B W W B B B
        W W B B W W W
        B B W W B B B
        W W B B W W W
        B B W B B B B
        """
        with self.assertRaises(BoardIsFull):
            self.strategy.return_column(board, self.color)
