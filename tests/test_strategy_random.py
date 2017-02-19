#!/usr/bin/env python
import unittest
import random
import mock
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from game.gameboard import ColumnIsFull
from game.first_non_full_column_strategy import FirstNonFullColumnStrategy
from board_builder import BoardBuilder

class TestRandomStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = FirstNonFullColumnStrategy()
        self.color = 'blue'
        self.builder = BoardBuilder('blue', 'red')

    def test_random_strategy_with_empty_board(self):
        def __return_one():
            return 1
        test_board = GameBoard()
        with mock.patch('random.random', __return_one):
            self.assertEqual(self.strategy.return_column(test_board, self.color), 1)

    def test_random_strategy_with_full_board(self):
        def __return_one():
            return 1
        test_board = self.builder.build_from_moves(
            [5,4,6,5,6,4,5,3,2,2,2,6,3,5,1,2,1,1,7,3,6,4,
             1,7,4,7,3,6,5,1,3,4,4,3,7,5,2,6,7,2,1,7])
        """
        B B R R B B B
        R R B B R R R
        B R R B B R B
        R R B R R R B
        B B R B B B R
        R R R B B R B
        """
        with mock.patch('random.random', __return_one):
            with self.assertRaises(BoardIsFull):
                self.assertEqual(self.strategy.return_column(test_board, self.color), 1)

    def test_random_strategy_with_only_one_column_available(self):
        """
        R B R . R R R
        B B R . B B B
        B R B B R R R
        R B B R B B R
        B R R B B R B
        B B R B R R R
        """
        test_board = self.builder.build_from_moves(
        [5,1,7,2,3,4,3,5,6,1,2,4,6,6,6,7,1,5,7,3,5,
         2,4,3,3,1,2,2,3,1,1,5,7,7,5,2,7,6,6,4])
        self.assertEqual(self.strategy.return_column(test_board, self.color), 4)
