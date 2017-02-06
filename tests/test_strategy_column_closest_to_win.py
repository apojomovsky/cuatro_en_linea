#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.strategy_column_closest_to_win import StrategyColumnClosestToWin

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy = StrategyColumnClosestToWin()
        self.color = 'blue'

    def test_strategy_choses_leftmost_column_from_empty_board(self):
        """return_column will chose the leftmost column from a group of same level
           columns. So in empty board, as all are the same, choses the leftmost one.
        """
        board = GameBoard()
        self.assertEqual(1, self.strategy.return_column(board, self.color))

    def test_strategy_choses_column_closest_to_win_for_blue(self):
        """return_column will chose column three because is the closest
           column to win for color blue"""
        board = GameBoard.from_matrix([
                    [None,  None,   None, None, None, None, None],
                    [None,  None,   None, None, None, None, None],
                    [None,  None,   None, None, None, None, None],
                    ['red', None,   None, None, None, None, None],
                    ['red', None, 'blue', None, None, None, None],
                    ['red', None, 'blue', None, None, None, None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 3)

    def test_strategy_choses_sixth_column_because_unable_to_win_on_leftmost(self):
        """return_column will chose column six because even while the first one is
           suppossed to be closer to win, it can't because of lack of free entries
        """
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None,  None,  None],
                    ['blue', None, None, None, None,  None,  None],
                    ['blue', None, None, None, None,  None,  None],
                    ['red',  None, None, None, None,  None,  None],
                    ['red',  None, None, None, None,  None,  None],
                    ['red',  None, None, None, None, 'blue', None]])
        self.assertEqual(6, self.strategy.return_column(board, self.color))

    def test_strategy_choses_leftmost_column_when_more_than_one_are_equal(self):
        """return_column will chose column three because, even while it and
           column four have the same ammount of blue chips, leftmost is priorized
        """
        board = GameBoard.from_matrix([
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None,   None,   None,  None, None,  None],
                    [None,   None, 'blue', 'blue',  None, None,  None],
                    ['red', 'red', 'blue', 'blue', 'red', 'red', None]])
        self.assertEqual(self.strategy.return_column(board, self.color), 3)

    def test_strategy_choses_first_non_full_column_when_unable_to_win(self):
        """If all the columns are unable to make a four-in-a-row, it will
           return the first non full column.
        """
        board = GameBoard.from_matrix([
                    [None,     None,   None,   None,   None,   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red',  'red'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertEqual(1, self.strategy.return_column(board, self.color))
