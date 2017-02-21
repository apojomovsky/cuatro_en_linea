#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.closest_to_win_column_strategy import ClosestToWinColumnStrategy
from board_builder import BoardBuilder

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy = ClosestToWinColumnStrategy()
        self.color = 'W'
        self.builder = BoardBuilder('W', 'B')
        self.strategy.prepare(self.color, None)

    def test_strategy_choses_leftmost_column_from_empty_board(self):
        """return_column will chose the leftmost column from a group of same level
           columns. So in empty board, as all are the same, choses the leftmost one.
        """
        board = GameBoard()
        self.assertEqual(1, self.strategy.return_column(board))

    def test_strategy_choses_closest_to_win_column_for_white(self):
        """return_column will chose column three because is the closest
           column to win for color white"""
        test_board = self.builder.build_from_moves([1,3,1,3,1,3])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W . . . . . .
        W . B . . . .
        W . B . . . .
        """
        self.assertEqual(1, self.strategy.return_column(test_board))

    def test_strategy_choses_sixth_column_because_unable_to_win_on_leftmost(self):
        """return_column will chose column fourth because even while the first one is
           supposed to be closer to win, it can't because of lack of free entries
        """
        test_board = self.builder.build_from_moves([1,1,4,1,1,2,1,2])
        """
        . . . . . . .
        W . . . . . .
        W . . . . . .
        B . . . . . .
        B B . . . . .
        W B . W . . .
        """
        self.assertEqual(4, self.strategy.return_column(test_board))

    def test_strategy_choses_leftmost_column_when_more_than_one_are_equal(self):
        """return_column will chose column three because, even while it and
           column four have the same ammount of black chips, leftmost is priorized
        """
        test_board = self.builder.build_from_moves([3,1,3,2,4,5,4,6])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . W W . . .
        B B W W B B .
        """
        self.assertEqual(3, self.strategy.return_column(test_board))

    def test_strategy_choses_first_non_full_column_when_unable_to_win(self):
        """If all the columns are unable to make a four-in-a-row, it will
           return the first non full column.
        """
        test_board = self.builder.build_from_moves(
        [6,4,7,3,2,1,5,4,5,4,3,1,1,6,1,6,5,6,7,2,7,1,4,7,2,7,3,3,6,2,2,5,5,4,3])
        """
        . . . . . . .
        B W W B W W B
        W B B W B B B
        W W W B W B W
        B B W B W B W
        B W B B W W W

        """
        self.assertEqual(1, self.strategy.return_column(test_board))
