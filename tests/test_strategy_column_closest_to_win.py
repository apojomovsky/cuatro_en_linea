#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.closest_to_win_column_strategy import ClosestToWinColumnStrategy

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy = ClosestToWinColumnStrategy()
        self.color = 'W'

    def test_strategy_choses_leftmost_column_from_empty_board(self):
        """return_column will chose the leftmost column from a group of same level
           columns. So in empty board, as all are the same, choses the leftmost one.
        """
        board = GameBoard()
        self.assertEqual(1, self.strategy.return_column(board, self.color))

    def test_strategy_choses_closest_to_win_column_for_black(self):
        """return_column will chose column three because is the closest
           column to win for color black"""
        board = GameBoard.from_matrix([
                    [None,  None,   None, None, None, None, None],
                    [None,  None,   None, None, None, None, None],
                    [None,  None,   None, None, None, None, None],
                    ['B', None,   None, None, None, None, None],
                    ['B', None, 'W', None, None, None, None],
                    ['B', None, 'W', None, None, None, None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 3)

    def test_strategy_choses_sixth_column_because_unable_to_win_on_leftmost(self):
        """return_column will chose column six because even while the first one is
           suppossed to be closer to win, it can't because of lack of free entries
        """
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None,  None,  None],
                    ['W', None, None, None, None,  None,  None],
                    ['W', None, None, None, None,  None,  None],
                    ['B',  None, None, None, None,  None,  None],
                    ['B',  None, None, None, None,  None,  None],
                    ['B',  None, None, None, None, 'W', None]])
        self.assertEqual(6, self.strategy.return_column(board, self.color))

    def test_strategy_choses_leftmost_column_when_more_than_one_are_equal(self):
        """return_column will chose column three because, even while it and
           column four have the same ammount of black chips, leftmost is priorized
        """
        board = GameBoard.from_matrix([
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None, 'W', 'W',  None, None,  None],
                    ['B', 'B', 'W', 'W', 'B', 'B', None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 3)

    def test_strategy_choses_first_non_full_column_when_unable_to_win(self):
        """If all the columns are unable to make a four-in-a-row, it will
           return the first non full column.
        """
        board = GameBoard.from_matrix([
                    [None,     None,   None,   None,   None,   None,   None],
                    ['B',   'B', 'W',  'B',  'B',  'B', 'W'],
                    ['B',  'W',  'B',  'B', 'W', 'W', 'W'],
                    ['W', 'W',  'B', 'W',  'B',  'B',  'B'],
                    ['B',  'W',  'B', 'W',  'B', 'W',  'B'],
                    ['W',  'B', 'W',  'B',  'B',  'B',  'B']])
        self.assertEqual(1, self.strategy.return_column(board, self.color))
