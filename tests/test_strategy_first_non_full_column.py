#!/usr/bin/env python
import unittest
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from board_builder import BoardBuilder
from game.first_non_full_column_strategy import FirstNonFullColumnStrategy
from board_builder import BoardBuilder

class TestFirstNonFullColumnStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = FirstNonFullColumnStrategy()
        self.color = 'W'
        self.builder = BoardBuilder('W', 'B')

    def test_strategy_choses_leftmost_column_on_empty_board(self):
        """
        This strategy returns the first column (leftmost)
        when the board is empty
        """
        board = GameBoard()
        self.assertEqual(self.strategy.return_column(board, self.color), 1)

    def test_strategy_on_near_empty_board(self):
        """
        The strategy looks from left to right for the first non-full column.
        The test expects the first column because it's not full.
        """
        test_board = self.builder.build_from_moves([1])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W . . . . . .
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 1)

    def test_strategy_on_near_full_column(self):
        """
        Even if the column is almost full, this strategy will choose it
        if it's the leftmost non full
        """
        test_board = self.builder.build_from_moves([1,1,1,1,1])
        """
        . . . . . . .
        W . . . . . .
        B . . . . . .
        W . . . . . .
        B . . . . . .
        W . . . . . .
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 1)

    def test_strategy_choses_leftmost_non_full_column(self):
        """
        This strategy will choose column two, because it's the leftmost column
        that is not full
        """
        test_board = self.builder.build_from_moves([1,1,1,1,1,1])
        """
        B . . . . . .
        W . . . . . .
        B . . . . . .
        W . . . . . .
        B . . . . . .
        W . . . . . .
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 2)

    def test_strategy_choses_the_only_non_full_column(self):
        """The strategy choses correctly the only column that is not full on the
           whole board
        """
        test_board = self.builder.build_from_moves(
            [3,4,6,7,5,6,2,2,6,1,5,3,7,6,3,7,6,2,7,
             5,1,1,7,3,5,5,2,4,1,3,6,1,2,2,1,4,7,5,3])

        """
        W B W . B W W
        B W B . B W W
        W W B . W B W
        B B W B B W B
        W B B B W B W
        B W W B W W B
        """
        self.assertEqual(self.strategy.return_column(test_board, self.color), 4)

    def test_strategy_raises_exception_on_full_board(self):
        """If it turns that the board is full, but the return_column message from
           the strategy is called, a BoardIsFull exception will be raised.
        """
        test_board = self.builder.build_from_moves(
            [3,7,1,3,2,4,1,4,5,1,5,5,7,5,5,6,4,3,6,7,7,
             6,2,4,4,3,1,2,5,1,2,2,3,7,6,1,2,6,4,6,7,3])
        """
        B W B W W B W
        B B W W W B B
        W W B B B W W
        B B B W B B B
        W W B B W W W
        """
        with self.assertRaises(BoardIsFull):
            self.strategy.return_column(test_board, self.color)
